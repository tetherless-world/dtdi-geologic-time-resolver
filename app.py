from flask import Flask, request, abort
import json

app = Flask(__name__)

with open("intervals.json") as b:
    data = json.load(b)


def intersects(interval, min_age, max_age):
    if interval["lag"] <= min_age <= interval["eag"]:
        return True
    elif interval["lag"] <= max_age <= interval["eag"]:
        return True
    elif interval["lag"] >= min_age and max_age >= interval["eag"]:
        return True
    else:
        return False


def resolve_geologic_time_intersects(min_age, max_age):
    z = [interval for interval in data["records"] if intersects(interval, min_age, max_age)]
    z.sort(key=lambda x: x["lag"])
    z.sort(key=lambda x: x["lvl"])
    return json.dumps(z)


def within(interval, min_age, max_age):
    return interval["lag"] <= min_age <= max_age <= interval["eag"]


def resolve_geologic_time_within(min_age, max_age):
    z = [interval for interval in data["records"] if within(interval, min_age, max_age)]
    z.sort(key=lambda x: x["lvl"], reverse=True)
    return json.dumps(z[0])


@app.route("/")
def hello():
    return json.dumps(data)


def process_inputs():
    min_age = request.args.get('min', None, type=float)
    max_age = request.args.get('max', None, type=float)

    if min_age is None or max_age is None:
        abort(400)

    return min_age, max_age


@app.route("/resolve-within", methods=['GET'])
def resolve_within():
    min_age, max_age = process_inputs()
    return resolve_geologic_time_within(min_age, max_age)


@app.route("/resolve-intersects", methods=['GET'])
def resolve_intersects():
    min_age, max_age = process_inputs()
    return resolve_geologic_time_intersects(min_age, max_age)


if __name__ == "__main__":
    app.run()
