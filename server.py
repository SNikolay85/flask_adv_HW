import json
from hashlib import md5

from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Session, Advert
from schema import CreateAdv, UpdateAdv

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: dict | str | list):
        self.status_code = status_code
        self.message = message


def validate(json_data, schema):
    try:
        model = schema(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as err:
        error_message = json.loads(err.json())
        raise HttpError(400, error_message)


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    http_response = jsonify({"status": "error", "message": er.message})
    http_response.status_code = er.status_code
    return http_response


def get_adv(adv_id: int, session: Session):
    advertisement = session.get(Advert, adv_id)
    if advertisement is None:
        raise HttpError(404, "advertisement not found")
    return advertisement


class AdvertView(MethodView):
    def get(self, adv_id):
        with Session() as session:
            advertisement = get_adv(adv_id, session)
            return jsonify({"id": advertisement.id, "header": advertisement.header})

    def post(self):
        json_data = validate(request.json, CreateAdv)
        with Session() as session:
            new_advertisement = Advert(**json_data)
            session.add(new_advertisement)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "advertisement already exists")
            return jsonify({"id": new_advertisement.id})

    def patch(self, adv_id):
        json_data = validate(request.json, UpdateAdv)
        # if "password" in json_data:
        #     json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            advertisement = get_adv(adv_id, session)
            for key, value in json_data.items():
                setattr(Advert, key, value)
            session.add(advertisement)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "header already exists")
            return jsonify({"status": "success"})

    def delete(self, adv_id):
        with Session() as session:
            advertisement = get_adv(adv_id, session)
            session.delete(advertisement)
            session.commit()
            return jsonify({"status": "success"})


adv_view = AdvertView.as_view("advertisement")

app.add_url_rule(
    "/advertisements/",
    view_func=adv_view,
    methods=["POST"])

app.add_url_rule(
    "/advertisements/<int:adv_id>",
    view_func=adv_view,
    methods=["GET", "PATCH", "DELETE"]
)

if __name__ == "__main__":
    app.run(port=8000)
