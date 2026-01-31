import json
# TODO решите задачу
def task() -> float:
    with open("input.json") as f:
        data = json.load(f)
        result = sum(el["score"] *
el["weight"] for el in data)
        return round(result, 3)


print(task())
