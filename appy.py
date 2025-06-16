import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision import models
import json
import requests

st.title("이미지 분류기 웹앱 🖼️")

# 사전 학습된 모델 불러오기
model = models.resnet18(pretrained=True)
model.eval()

# 이미지 전처리 함수
def preprocess(image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])
    return transform(image).unsqueeze(0)

# ImageNet 클래스 라벨 다운로드
@st.cache_data
def load_labels():
    url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    response = requests.get(url)
    classes = response.text.strip().split("\n")
    return classes

classes = load_labels()

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="업로드된 이미지", use_column_width=True)

    input_tensor = preprocess(image)
    
    with torch.no_grad():
        outputs = model(input_tensor)
    
    # 가장 높은 확률을 가진 클래스 추출
    _, predicted_idx = torch.max(outputs, 1)
    predicted_label = classes[predicted_idx]

    st.write(f"예측 결과: **{predicted_label}**")
