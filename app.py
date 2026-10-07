import random
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

st.title("HOUSE OF TABBY: SPIRIT GAME")

# Kho ảnh Pixel Art Kinh dị
IMG_ROOM = "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800"
IMG_HALLWAY = "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=800"
IMG_LOCKER = "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800"
IMG_ENEMY = "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=800"

# Khởi tạo dữ liệu Game
if "location" not in st.session_state:
    st.session_state.location = "room"
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
    st.session_state.time_survived += 1

    if random.random() < 0.4 and not st.session_state.generator_broken:
        st.session_state.generator_broken = True

    if random.random() < 0.5:
        st.session_state.villain_near = True
    else:
        st.session_state.villain_near = False

    if st.session_state.time_survived >= 8:
        st.session_state.win = True


# MÀN HÌNH KẾT THÚC
if st.session_state.game_over:
    st.image(
        IMG_ENEMY,
        caption="KE PHAN DIEN DA TOI... GAME OVER!",
        use_container_width=True,
    )
    st.error("Ban da bi phát hien!")
    if st.button("CHOI LAI"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.win:
    st.balloons()
    st.success("CHIEN THANG! BAN DA SONG SOT QUA DEM!")
    if st.button("CHOI LAI"):
        st.session_state.clear()
        st.rerun()

else:
    st.caption(
        f"Luot song sot: {st.session_state.time_survived}/8 | Style: Tabby House Pixel"
    )

    # ĐỊA ĐIỂM: PHÒNG TRỰC
    if st.session_state.location == "room":
        st.image(
            IMG_ROOM,
            caption="Phong An Toan (Co Tu Tron)",
            use_container_width=True,
        )

        if st.session_state.generator_broken:
            st.error(
                "BAO DONG: May phat dien hanh lang bi hong! Mat dien toan he thong!"
            )
        elif st.session_state.villain_near:
            st.warning(
                "CANH BAO: Co tieng buoc chan nang ne dang tien gan phong..."
            )
        else:
            st.info("Bau khong khi im lang den ron nguoi...")

        st.write("---")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("CHUI VAO TU TRON"):
                st.session_state.location = "locker"
                st.rerun()

        with col2:
            if st.button("RA HANH LANG KIEM TRA"):
                st.session_state.location = "hallway"
                st.rerun()

        with col3:
            if st.button("CHO VA QUAN SAT"):
                if st.session_state.villain_near:
                    st.session_state.game_over = True
                else:
                    trigger_event()
                st.rerun()

    # ĐỊA ĐIỂM: TỦ TRỐN
    elif st.session_state.location == "locker":
        st.image(
            IMG_LOCKER,
            caption="Ban dang nin tho ben trong chiec tu go chat hep...",
            use_container_width=True,
        )

        if st.session_state.villain_near:
            st.error(
                "Ke phan dien vua di ngang qua tu... Ban nghe thay tieng tho cua no!"
            )
        else:
            st.write("Ben ngoai co ve da an toan.")

        st.write("---")
        if st.button("BUOC RA KHOI TU"):
            st.session_state.location = "room"
            st.session_state.villain_near = False
            trigger_event()
            st.rerun()

    # ĐỊA ĐIỂM: HÀNH LANG KIỂM TRA SỰ CỐ
    elif st.session_state.location == "hallway":
        st.image(
            IMG_HALLWAY,
            caption="Hanh lang toi - Noi dat May phat dien",
            use_container_width=True,
        )

        if st.session_state.villain_near:
            st.error(
                "BONG DEN PHAN DIEN XUAT HIEN TU CUOI HANH LANG! CHAY NGAY!"
            )

        st.write("---")
        col_h1, col_h2 = st.columns(2)

        with col_h1:
            if st.session_state.generator_broken:
                if st.button("SUA MAY PHAT DIEN"):
                    if st.session_state.villain_near:
                        st.session_state.game_over = True
                    else:
                        st.session_state.generator_broken = False
                        st.success("Ban da sua xong may phat dien!")
                        trigger_event()
                    st.rerun()
            else:
                st.write("May phat dien dang hoat dong binh thuong.")

        with col_h2:
            if st.button("CHAY VE PHONG TRUC"):
                st.session_state.location = "room"
                st.rerun()
