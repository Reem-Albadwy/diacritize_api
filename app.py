from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

class RequestBody(BaseModel):
    text: str


@app.post("/diacritize")
def diacritize(req: RequestBody):

    prompt = f"""
أضف التشكيل الكامل للنص العربي التالي مع مراعاة المعنى:
{req.text}
أعد النص فقط بعد التشكيل بدون أي شرح.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {"result": response.text}
