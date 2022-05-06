from fastapi import FastAPI, HTTPException


from app.utils import Field

app = FastAPI()
fields = {}


@app.post("/create_field")
async def create_field():
    field = Field()

    if fields.keys():
        new_key = sorted(fields.keys())[-1] + 1  # find last key and increment
    else:
        new_key = 1

    fields[new_key] = field

    return {"id": new_key, "field": field.field}


@app.get("/step/{field_id}")
async def field_step(field_id: int):
    try:
        field = fields[field_id]
        field.step()
        return {"id": field_id, "field": field.field}
    except KeyError:
        raise HTTPException(status_code=404, detail="Field not found")
