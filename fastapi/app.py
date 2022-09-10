from fastapi import FastAPI, Form, UploadFile, File
from model import impute
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/upload", response_class=FileResponse)
async def upload(crop = Form(), region = Form(), vcf: UploadFile = File()):
    print("Message have recieved from Streamlit")
    
    content = await vcf.read()
    out_path = impute(crop, region, content)

    return out_path