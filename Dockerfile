#Base Image to use
FROM python:3.12

EXPOSE 8080
WORKDIR /genai4datasec
COPY . ./

#install all requirements in requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup
CMD ["python3", "main.py"]
