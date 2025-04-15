
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="پیش‌بینی فروش فروشگاه", layout="centered")
st.title("📊 پیش‌بینی فروش روزانه فروشگاه پوشاک (مدل محدودشده)")

# بارگذاری مدل محدودشده
model = joblib.load("model_xgboost_monotonic.pkl")

# تعریف پارامترها به ترتیب آموزش مدل
params = {
    'جمعیت': None,
    'متراژ سطح فروش': None,
    'فرهنگ (نوع پوشش)': None,
    'وضعیت رقبا (بازار بکر)': None,
    'وضعیت اقتصادی': None,
    'سطح رفاه مردم منطقه': None,
    'خیابان (اصلی/فرعی، یک‌طرفه/دوطرفه، عرض خیابان)': None,
    'نزدیکی به بازارهای پوشاک': None,
    'گذر ماشین': None,
    'پاخور پیاده': None,
    'جای پارک ماشین': None,
    'تراکم جمعیت منطقه': None,
    'دید و رخ تابلو': None,
    'المان‌های بصری (لایت‌باکس، آینه، رنگ داخلی و...)': None,
    'وضعیت نور داخلی': None,
    'ارتفاع سقف': None,
    'بحر مغازه': None,
    'جذابیت بصری و ظاهری': None,
}

st.markdown("اعداد بین 0 تا 10 وارد کنید:")

for key in params:
    params[key] = st.number_input(key, min_value=0.0, max_value=10.0, value=5.0, step=0.1)

if st.button("🔍 پیش‌بینی فروش"):
    input_array = np.array([list(params.values())])
    predicted = model.predict(input_array)[0]
    st.success(f"📈 فروش پیش‌بینی‌شده: {predicted:,.0f} میلیون تومان")
