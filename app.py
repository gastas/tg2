import streamlit as st
import io
import os
import datetime
import extra_streamlit_components as stx
import telebot

def get_manager():
    return stx.CookieManager()


st.set_page_config(
     page_icon="🖱️", page_title="Отзывы"
)
st.title("Добавьте свой отзыв")


cookie_manager = get_manager()
submissions = cookie_manager.get(cookie='submissions')
if submissions is None:
    cookie_manager.set('submissions', 0)

else:
    submissions = int(cookie_manager.get(cookie='submissions'))
    if submissions > 0:
        st.success('Спасибо, вы уже отправили отзыв', icon="✅")

fio = st.text_input('ФИО (необязательно)', '')
txt = st.text_area('Отзыв','')
phone = st.text_input('Номер телефона (необязательно)','')
sklad = st.selectbox(
    'Склад',
    ('Пушкино', 'Шарапово'))

if st.button('Отправить'):
    if txt == '':
        st.error('Поле отзыв обязательно для заполнения')
    else:
        submissions = int(cookie_manager.get(cookie='submissions')) + 1
        # review = {'fio': fio, 'txt': txt, 'phone': phone, 'sklad': sklad, 'submission': submissions}
        token = st.secrets['telegram_bot']
        bot = telebot.TeleBot(token)
        chat_id = '-985714611'
        text = "ФИО: " + fio + "\nОтзыв: " + txt + "\nТелефон: " + phone + "\nСклад: " + sklad + "\nОтзывов у пользователя: " + str(submissions)
        bot.send_message(chat_id, text)
        cookie_manager.set('submissions', submissions)
    
