import streamlit as st

st.title("🌸学生 小红-数字档案")
st.header("☘️基础信息")
st.text("学生ID：NEO-2025-026")
st.markdown("**注册时间:,':green[2025-10-20 11:13:12]'|精神状态:✅正常**")
st.markdown("**当前教室:,':green[实训楼204]’|安全等级:,':green[绝密]'**")            
st.header("🌲技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="绘画",help='技能', value="75%", delta="3%")
c2.metric(label="声乐",help='技能', value="78%", delta="-2%")
c3.metric(label="舞蹈",help='技能', value="76%", delta="6%")
st.header("🌳任务日志")
data = {
    '日期':["2025-10-5", "2025-10-15", "2025-10-20"],
    '任务':["绘画", "声乐", "舞蹈"],
    '状态':["✅完成", "🕐进行中", "❌未完成"],
    '难度':["⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"],
}
index = pd.Series(["0", "1", "2"],name="序号")
df = pd.DataFrame(data, index=index)
st.subheader('默认显示')
st.dataframe(df)
st.subheader('设置宽度和高度')
st.dataframe(df, width=400, height=150)
st.header("🌴最新代码成果")
python_code = '''def hello():
    print("你好，Streamlit！")
'''
st.code(python_code, language=None)
st.code(python_code)
st.code(python_code, line_numbers=True)
st.write(":green[>> SYSTEM MESSAGE:] 下一个任务目标已解锁...")
st.write(":green[>> TARGET:] 课程管理系统")
st.write(":green[>> COUNTDOWN:] 2025-10-20 14:50:20")
st.write("系统状态:在线 连接状态:已加密")
