from fastapi import FastAPI
from detonv import load_dotenv

app = FastAPI()

load_dotenv()

@app.get("/llm{promt}")
async def read_root(promt):
    #Crear una logica que me permita comunicarme con un llm
        
    from google import genai

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=promt
    )
    print(response.text)
    return {"Hello": response.text} 




