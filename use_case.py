#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from fastapi import FastAPI, HTTPException, UploadFile
from loguru import logger

UNOSERVER_ENDPOINT = "http://127.0.0.1"
app = FastAPI()


@app.post("/convert_ppt_to_pdf/")
async def conv_ppt_to_pdf(file: UploadFile):
    """Convert ppt to pdf"""
    logger.info(f"ppt parse start:{file.filename=}")
    in_file_bytes = await file.read()
    try:
        uno_client = UnoClient(UNOSERVER_ENDPOINT, port="2003")
        pdf_file_bytes = uno_client.convert(indata=in_file_bytes, convert_to='pdf')
        logger.info(f"ppt parse completed:{file.filename=}")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=409, detail="ppt2pdf failed")
    return Response(content=pdf_file_bytes, media_type="application/pdf")
