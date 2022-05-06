# Game of Life service
## Rules:
### Игра «Жизнь» (англ. Conway's Game of Life) — клеточный автомат, придуманный английским математиком Джоном Конвеем в 1970.
1.  Действие происходит на бесконечной плоскости, разделенной на клетки, которую можно иногда представить как зацикленную конечную.
2.  Каждая клетка может находиться в двух состояниях: быть живой или быть мёртвой.
3.  У каждой клетки 8 соседей.
4.  Если клетка жива и у нее 2−3 живых соседа, то она остается живой, иначе умирает.
5.  Если клетка мертва и у нее 3 живых соседа, то она становится живой, иначе остается мертвой.

## How run this project?
## Firstly install dependencies with poetry
```shell
cd app && poetry install
```
## Then run service with command below
```shell
uvicorn app.main:app
```
## After server start go to http://127.0.0.1:8000/docs and check available methods with pretty UI

## Also, you can run tests and check code coverage
```shell
coverage run -m pytest ./tests/tests.py
coverage report
```

## My algorithm realised in Field class located in app.utils 
