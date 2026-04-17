from dotenv import load_dotenv
from prisma import Prisma
from flask import jsonify
import asyncio

from app import create_app

# load environment variables
load_dotenv()

app = create_app()

@app.route("/", methods=["GET"])
async def home():
    prisma = Prisma()
    try:
        await prisma.connect()

        student = await prisma.student.find_first()

        if student:
            return jsonify(student.model_dump())
        else:
            return jsonify({"message": "No student found"})

    finally:
        await prisma.disconnect()


if __name__ == "__main__":
    app.run(debug=True)