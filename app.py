import random
import streamlit as st

st.set_page_config(
    page_title="Đêm Trực 0:00 AM", page_icon="🧸", layout="centered"
)

# Giao diện u tối chuẩn FNAF / Little Nightmares
st.markdown(
    """
    <style>
    .stApp { background-color: #08080a; color: #a6a6a6; }
    h1 { color: #cc0000 !important; text-shadow: 0px 0px 10px #ff0000; }
    .stButton>button {
        background-color: #1a0000; color: #ff9999; border: 1px solid #800000;
        width: 100%; border-radius: 4px; padding: 10px; font-weight: bold;
    }
    .stButton>button:hover { background-color: #ff0000; color: #ffffff; }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🧸 GAME SPIRIT: ĐÊM TRỰC 0:00 AM")
st.caption(
    "Lấy cảm hứng từ FNAF & Little Nightmares | Sống sót đến 6:00 AM để chiến thắng"
)

# Khởi tạo trạng thái game
if "time" not in st.session_state:
    st.session_state.time = 0  # 0h -> 6h
if "battery" not in st.session_state:
    st.session_state.battery = 100
if "monster_distance" not in st.session_state:
    st.session_state.monster_distance = 3  # 3: Xa, 2: Gần, 1: Ngay cửa
if "door_closed" not in st.session_state:
    st.session_state.door_closed = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "win" not in st.session_state:
    st.session_state.win = False


def next_hour():
    st.session_state.time += 1
    st.session_state.battery -= random.randint(12, 20)

    # Quái vật tiến lại gần nếu cửa mở
    if not st.session_state.door_closed:
        st.session_state.monster_distance -= random.randint(1, 2)
    else:
        # Đóng cửa thì quái bị đuổi lùi lại
        st.session_state.monster_distance = 3
        st.session_state.battery -= 10  # Đóng cửa tốn thêm pin

    # Kiểm tra điều kiện thua
    if st.session_state.monster_distance <= 0 and not st.session_state.door_closed:
        st.session_state.game_over = True
    elif st.session_state.battery <= 0:
        st.session_state.game_over = True
        st.session_state.battery = 0
    elif st.session_state.time >= 6:
        st.session_state.win = True


# MÀN HÌNH THẮNG / THUẤ
if st.session_state.game_over:
    st.error("😱 JUMPSCARE! CON QUÁI VẬT TAY DÀI ĐÃ TỚI!")
    st.write(
        "Màn hình tắt phụt... Một tiếng rít xé óc vang lên ngay sát tai bạn."
    )
    if st.button("🔄 Thử lại đêm khác"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.win:
    st.balloons()
    st.success("🎉 6:00 AM - BẠN ĐÃ SỐNG SÓT QUA ĐÊM KINH HOÀNG!")
    if st.button("🔄 Chơi lại"):
        st.session_state.clear()
        st.rerun()

else:
    # HIỂN THỊ THÔNG TIN
    col1, col2, col3 = st.columns(3)
    col1.metric("⏰ Thời gian", f"{st.session_state.time}:00 AM")
    col2.metric("🔋 Pin còn lại", f"{st.session_state.battery}%")
    col3.metric(
        "🚪 Trạng thái cửa",
        "ĐÓNG" if st.session_state.door_closed else "MỞ",
    )

    st.write("---")

    # BÁO ĐỘNG KHI QUÁI TỚI GẦN
    if st.session_state.monster_distance == 3:
        st.info("📺 Camera 01: Hành lang yên tĩnh. Có tiếng kim loại va chạm từ xa...")
    elif st.session_state.monster_distance == 2:
        st.warning(
            "⚠️ Camera 02: BÓNG ĐEN TAY DÀI ĐANG BÒ TRÊN TRẦN NHÀ HÀNH LANG!"
        )
    elif st.session_state.monster_distance == 1:
        st.error(
            "🚨 NGUY HIỂM: NÓ ĐANG ĐỨNG NGAY NGOÀI CỬA PHÒNG TRỰC! NÍN THỞ!"
        )

    st.write("")

    # HÀNH ĐỘNG
    col_a, col_b = st.columns(2)

    with col_a:
        if st.session_state.door_closed:
            if st.button("🔓 Mở cửa phòng (Tiết kiệm pin)"):
                st.session_state.door_closed = False
                st.rerun()
        else:
            if st.button("🔒 ĐÓNG CỬA NGAY! (Tốn pin)"):
                st.session_state.door_closed = True
                st.rerun()

    with col_b:
        if st.button("👀 Chờ qua giờ tiếp theo"):
            next_hour()
            st.rerun()
