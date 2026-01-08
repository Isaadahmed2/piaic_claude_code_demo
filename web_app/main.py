from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import math
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="web_app/static"), name="static")
templates = Jinja2Templates(directory="web_app/templates")

class CalculationRequest(BaseModel):
    operation: str
    a: float
    b: Optional[float] = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate(request: CalculationRequest):
    try:
        a = request.a
        b = request.b
        op = request.operation

        if op == 'add':
            return {"result": a + b}
        elif op == 'subtract':
            return {"result": a - b}
        elif op == 'multiply':
            return {"result": a * b}
        elif op == 'divide':
            if b == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")
            return {"result": a / b}
        elif op == 'modulo':
            if b == 0:
                raise HTTPException(status_code=400, detail="Cannot compute modulo by zero")
            return {"result": a % b}
        elif op == 'power':
            return {"result": a ** b}
        elif op == 'sqrt':
            if a < 0:
                raise HTTPException(status_code=400, detail="Cannot compute square root of negative number")
            return {"result": math.sqrt(a)}
        elif op == 'factorial':
            if a < 0 or not float(a).is_integer():
                raise HTTPException(status_code=400, detail="Factorial requires non-negative integer")
            return {"result": math.factorial(int(a))}
        elif op == 'log':
            if a <= 0:
                raise HTTPException(status_code=400, detail="Logarithm argument must be positive")
            return {"result": math.log(a)}
        elif op == 'sin':
            return {"result": math.sin(math.radians(a))}
        elif op == 'cos':
            return {"result": math.cos(math.radians(a))}
        elif op == 'tan':
            return {"result": math.tan(math.radians(a))}
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
