import random
import streamlit as st

# Khởi tạo danh sách số từ 1 đến 7, sử dụng `st.session_state` để lưu danh sách giữa các lần chạy
if 'numbers' not in st.session_state:
    st.session_state.numbers = list(range(1, 6))

st.title("CHỌN TEAM NAM - NỮ")

# Tạo nút quay số
if st.session_state.numbers:
    if st.button('XIN MỜI ANH CHỌN'):
        chosen_number = random.choice(st.session_state.numbers)
        st.session_state.numbers.remove(chosen_number)
        st.write(f"CẢM ƠN ANH ĐÃ CHỌN EM: {chosen_number}")
        st.write(f"TRONG KHO CÒN CÁC EM...: {st.session_state.numbers}")
else:
    st.write("KHÔNG CÒN EM NÀO ĐỂ CHỌN NỮA RỒI ")
    st.button('HẸN GẶP LẠI ANH', disabled=True)  # Vô hiệu hóa nút sau khi hết số