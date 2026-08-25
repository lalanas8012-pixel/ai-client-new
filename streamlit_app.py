import streamlit as st

st.set_page_config(
    page_title="AI 모의내담자",
    page_icon="💬"
)

st.title("💬 AI 모의내담자 상담실")
st.caption("상담자 훈련을 위한 연구용 프로토타입")

st.write("아래 채팅창에 상담자로서 말을 입력해보세요.")

message = st.chat_input("상담자의 반응을 입력하세요")

if message:
    with st.chat_message("user"):
        st.write(message)

    with st.chat_message("assistant"):
        st.write("음... 잘 모르겠어요. 요즘 그냥 조금 지쳐 있는 것 같아요.")
        