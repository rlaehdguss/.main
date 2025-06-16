import streamlit as st

st.title("간단 퀴즈 앱 🎉")

# 문제와 답
question = "한국의 수도는 어디일까요?"
options = ["부산", "서울", "대구", "인천"]
answer = "서울"

# 사용자가 선택할 수 있게 라디오 버튼 생성
user_answer = st.radio("아래 보기 중 하나를 선택하세요:", options)

# 제출 버튼
if st.button("제출"):
    if user_answer == answer:
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸어요. 다시 시도해보세요!")
