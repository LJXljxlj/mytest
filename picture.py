import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

images = [
    {
        'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
        'parm':'鸟'
    },
    {
        'url':'https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg',
        'parm':'狗'
    },
    {
        'url':'https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg',
        'parm':'猫'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])
c1, c2 = st.columns(2)
with c1:
    st.button('上一张', on_click=prevImg, use_container_width=True)
with c2:
    st.button('下一张', on_click=nextImg, use_container_width=True)

