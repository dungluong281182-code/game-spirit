import random
import time
import streamlit as st

st.set_page_config(
    page_title="GAME SPIRIT: HOUSE OF SPIRITS", page_icon="🏚️", layout="centered"
)

# Style Đồ họa Pixel Retro / Tabby House
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .stApp {
        background-color: #0b090a;
        color: #d3d3d3;
        font-family: 'Press Start 2P', monospace;
    }
    h1 {
        font-family: 'Press Start 2P', monospace !important;
        color: #e63946 !important;
        text-shadow: 3px 3px 0px #1d3557;
        font-size: 1.5rem !important;
        text-align: center;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #161a1d;
        color: #f1faee;
        border: 2px solid #e63946;
        padding: 10px;
        font-family: 'Press Start 2P', monospace;
        font-size: 0.7rem;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #e63946;
        color: #000000;
    }
    .stImage img {
        border: 4px solid #457b9d;
        image-rendering: pixelated;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🏚️ GAME SPIRIT: HOUSE OF TABBY")

# Kho ảnh Pixel Art Kinh dị (Minh họa phong cách House/Tabby)
IMG_ROOM = "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800"  # Phòng trực Pixel
IMG_HALLWAY = "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=800"  # Hành lang sửa máy
IMG_LOCKER = "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800"  # Trong tủ tối om
IMG_ENEMY = "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=800"  # Kẻ phản diện bóng đen

# Khởi tạo dữ liệu Game
if "location" not in st.session_state:
    st.session_state.location = "room"  # room, hallway, locker
if "generator_broken" not in st.session_state:
    st.session_state.generator_broken = False
if "villain_near" not in st.session_state:
    st.session_state.villain_near = False
if "time_survived" not in st.session_state:
    st.session_state.time_survived = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "win" not in st.session_state:
    st.session_state.win = False


def trigger_event():
    # Tăng thời gian
    st.session_state.time_survived += 1

    # Ngẫu nhiên hỏng máy phát điện
    if random.random() < 0.4 and not st.session_state.generator_broken:
        st.session_state.generator_broken = True

    # Ngẫu nhiên Kẻ phản diện xuất hiện
    if random.random() < 0.5:
        st.session_state.villain_near = True
    else:
        st.session_state.villain_near = False

    # Thắng sau 8 lượt sống sót
    if st.session_state.time_survived >= 8:
        st.session_state.win = True


# MÀN HÌNH KẾT THÚC
if st.session_state.game_over:
    st.image(
        IMG_ENEMY,
        caption="😱 KẺ PHẢN DIỆN ĐÃ TỚI... GAME OVER!",
        use_container_width=True,
    )
    st.error("💀 Bạn đã bị phát hiện!")
    if st.button("🔄 CHƠI LẠI"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.win:
    st.balloons()
    st.success("🎉 CHIẾN THẮNG! BẠN ĐÃ SỐNG SÓT QUA ĐÊM TRONG CĂN NHÀ!")
    if st.button("🔄 CHƠI LẠI"):
        st.session_state.clear()
        st.rerun()

else:
    st.caption(
        f"⏱️ Đã sống sót: {st.session_state.time_survived}/8 Lượt | 🕹️ Style: House/Tabby Pixel"
    )

    # ĐỊA ĐIỂM: PHÒNG TRỰC
    if st.session_state.location == "room":
        st.image(
            IMG_ROOM,
            caption="📺 Phòng An Toàn (Có Tủ Trốn 🗄️)",
            use_container_width=True,
        )

        if st.session_state.generator_broken:
            st.error(
                "🚨 BÁO ĐỘNG: Máy phát điện hành lang bị hỏng! Mất điện toàn hệ thống!"
            )
        elif st.session_state.villain_near:
            st.warning(
                "⚠️ CẢNH BÁO: Có tiếng bước chân nặng nề đang tiến gần phòng..."
            )
        else:
            st.info("Bầu không khí im lặng đến rợn người...")

        st.write("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🗄️ CHUI VÀO TỦ TRỐN"):
                st.session_state.location = "locker"
                st.rerun()

        with col2:
            if st.button("🚶 RA HÀNH LANG KIỂM TRA"):
                st.session_state.location = "hallway"
                st.rerun()

        with col3:
            if st.button("👀 CHỜ VÀ QU
