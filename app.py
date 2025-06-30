from flask import Flask, render_template, request,jsonify
from generateReport import generateReport
app = Flask(__name__)

def extract_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        removes = 0
        for i in range(len(lines)-1):
            if not lines[i-removes]:
                lines.remove(lines[i-removes])
                removes += 1
            if lines[i-removes][-1] == ":":
                lines[i-removes]=lines[i-removes][:-1]
    return lines

def calculate_score(list,index=4,weight=[0.3,0.2,0.3,0.2]):
    scorefive = 0
    for i in range(index):
        scorefive+=float(list[i])*weight[i]
    
    scorefive = round(scorefive,1)
    scorethirty = scorefive*5 + 5
    scorethirty = round(scorethirty,0)
    return [scorethirty,scorefive]
def extract_answer_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        lines = ['Answers List'] + lines
        return lines
file_path = 'static/table/2023_AcaTalk.txt '
result = extract_data_from_file(file_path)
print(len(result))
@app.route('/choose_paper', methods=['POST'])
def choose_paper():
    # try:
    if True:
        global question_num
        question_num = int(request.form.get("paperNumber"))
        
        
        global question
        question = [result[6*(question_num-1)+i] for i in range(0,6)]
        global nameA,nameB
        nameA, nameB, nameTea = question[2], question[4], question[0]
        stuA, stuB, tea = question[3], question[5], question[1]
        
        import time
        print(question)
        current_timestamp = time.time()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_timestamp))
        

        return jsonify({
            "status": "success",
            "data": {
                "stuB": stuB,
                "stuA": stuA,
                "tea": tea,
                "nameA": nameA,
                "nameB": nameB,
                "nameTea": nameTea,
                "questionNum": question_num,
                "time": current_time,
                "stamp": current_timestamp
            }
        })
        
    # except ValueError:
    #     return "Invalid paper number", 400
    # except Exception as e:
    #     return f"Error: {str(e)}", 500
@app.route('/')
def view():
    return render_template('view.html')

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    global toEvaluateAnswer
    toEvaluateAnswer = request.form.get('answer')
    from openai import OpenAI

    import os

    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    toEvaluateProblem = question

    exampleQuestion1: str = "Dr.    qAchebe \
    This week we analyzed some aspects of current educational systems. One type of school system we discussed was boarding schools, which, as the name suggests,is a type of school where students live during the school year. I would like you to discuss whether you consider boarding schools beneficial for students education or whether you think day schools, or.schools where students do not liveat the schools,are better formost students.Explain why you think so. \
    Claire \
    I would have loved to have attended aboarding school.I feel like board- ing schools would have helped me establish a strict daily routineand helped me become more disciplined. Also, being in a boarding school means that you are with friends and classmates around the clock,and I would have loved such an opportunity. \
    Andrew \
    I personally do not support the boarding school system as I believe it can lead to many psychological problems. In fact, I have heard about what is referred to as 'boarding school syndrome', which, in simple terms, suggests that some students who attend boarding schools at a very young age can have long-term emotional or behavioral challenges. So why take that risk if most students can just go to ordinary schools?"
    exampleAnswer1: str = "I am more inclined to agree that a boarding school system is beneficial.Firstly,a boarding school is a place whereyou can make friends with your classmates The 'roommate'relationship is somewhat strong that you may remember forever, as you wake up, eat meals, study, and go to sleep together with your roommates onevery school days. Secondly,a boarding school is usually close to your school campus, which means that you donot need to commute to and from school every day.Thirdly ,a boarding school is not a placemerelyfora disciplined life; it often conducts various activities to help you get immersed in the living environment and make your lifemore colorful, which cannot be experienced at home.I personally do not agree with Andrew's point that boarding school places high mental pressure on students, as boarding schools are not prisons and students are still free to leave on weekends to bond with their family and pursue their interests."
    exampleAnswer_4: str = "I personally do not support the idea of boarding school. Ibelieve that the boarding school system would cause more problems in their future. The idea of being away from your family would definitely effect of connectivity amongst them.S ending your child to a boarding school would just mean that you're leaving them with someone else,and anything can happen and th eparents won't know about it ,also I think that being confined into the same environment could effect the child's creativity and also social skills.making new friends, having new personalities around you and exploring new hobbiesthat children should experience are what makes them grow into a more mature and also diffren."
    exampleAnswer_3: str ="I think boarding school is in the most interest of the students, cause they can develop some good routine, learn from each other, share their interest for commun things, discover other culture.In boarding school,the students can bemore focuson the school and have better grades. Boarding school can also help the students to develop their sense offriendship, they learn they can count one on eachother and they should help each other in every situation."
    exampleQuestion2: str = "Doctor Achebe: \
    As of this semester, I have embarked on a study to explore the various factors influencing children's cognition. It's becoming increasingly evident that a child's surroundings can significantly impact their development. In light of this, the question arises: should parents allow their children to watch online videos, whether for entertainment or educational purposes? Please share your insights on this matter, considering the potential effects on a child's cognitive growth. \
    Andrew: \
    We should not allow young children, especially those under two years old, to watch videos. It's crucial for their development to engage in real-life communication with others during this critical period. Watching videos doesn't provide the opportunity for meaningful interaction. Even for older children, it's essential to prioritize physical activity over extended screen time. Instead of sitting still in front of screens, they should be encouraged to stay active to support their overall well-being. \
    Kelly:  \
    I agree that very young children shouldn't be exposed to videos. However, I believe that older children can benefit from watching certain videos, especially those that showcase animals or provide unique insights not easily encountered in everyday life. These videos can be educational and expand their horizons by offering a window into experiences they might not otherwise have access to."

    exampleAnswer2: str = " I am more inclined to agree that a boarding school system is beneficial.Firstly,a boarding school is a place whereyou can make friends with your classmates The 'roommate'relationship is somewhat strong that you may remember forever, as you wake up, eat meals, study, and go to sleep together with your roommates onevery school days. Secondly,a boarding school is usually close to your school campus, which means that you donot need to commute to and from school every day.Thirdly ,a boarding school is not a placemerelyfora disciplined life; it often conducts various activities to help you get immersed in the living environment and make your lifemore colorful, which cannot be experienced at home.I personally do not agree with Andrew's point that boarding school places high mental pressure on students, as boarding schools are not prisons and students are still free to leave on weekends to bond with their family and pursue their interests."
    
    system_prompt = f"你现在是一名托福考官，需要给学术讨论话题评分，严格评分。以下是一些评分标准：对观点的论述要详尽深入，有效表达至少80词才算论述完整，对重复观点而不举例子说明或进一步解释的要在逻辑分中扣分，注意事项如下：\
                1.请以托福官方评分标准为基准打分 \
                请你输出以下内容，严格按照以下标准：从4个部分（A内容相关度，B观点展开，C语言表达，D逻辑结构）分别给出5分制，范围在0.0-5.0之间的评分，,对A、B、D三个部分来说， \
                基于我的文章（不要改变大概的思路结构）给出一些可行的修改建议，对于C来说，修改错词，并给出一些重复词和过于简单的词的替换词(至少4组，每一组给出至少两个替换词)，最终输出一篇相对完整的文章，限制在190单词以内且符合你的建议，不要用数据论证。 \
                输出格式如下：\
                [A项的5分分数]@@@[B项的5分分数]@@@[C项的5分分数]@@@[D项的5分分数]@@@[A的问题]@@@[B的问题]@@@[C的问题]@@@[D的问题]@@@[A的优化方案]@@@[B的优化方案]@@@[C的优化方案]@@@[D的优化方案]@@@[最后呈现的文章] \
                注意事项： 2. 所有5分分数直接显示成x.x的一位小数浮点格式(如4.2) 3. 请将生成的相应内容替换回答中的[]内容 4. 其中不同内容直接像上方一样使用'@@@'连接，便于分割 5. 所有换行符请替换成'***'，便于识别，不要直接换行！ 6.除了文章、引用文章、替换词使用英文外，其他请用中文 7.使用单引号而非双引号 8. 严格按照以上的格式，不要添加其他内容！\
                输入格式(非内容)样例：4.0@@@3.8@@@3.5@@@3.8@@@1. 未直接回应教授问题的'positive/negative'核心框架***2. 企业案例与个人网购的衔接不够紧密@@@1. 企业案例缺少对'效率提升'的具体解释***2. 个人网购段落缺乏对'安全保障'的展开@@@1. 拼写错误：internat→internet***2. 重复词：definitely(3次)→certainly/unquestionably***3. 基础词：good→commodity/product***4. 简单词：make→facilitate/enable@@@1. 段落间过渡生硬***2. 结论缺乏分论点总结@@@A. 在首段明确立场'This is undoubtedly positive'***B. 增加过渡句'While corporate benefits are evident, individuals also gain...'@@@B. 解释'跨国支付如何缩短交易时间'***说明'支付安全如何防止欺诈'@@@C. 错误修正：***1. evlution→evolution***2. boarder→boundaries***3. perchase→purchase***4. sonsiderably→considerably***替换建议：***1. definately→undoubtedly/certainly***2. payment→transaction/digital currency***3. improve→enhance/optimize***4. range→spectrum/diversity@@@D. 添加连接词'Furthermore/Moreover'***结论总结分论点'global accessibility and personal convenience'@@@In the internet era, the evolution of payment systems has undoubtedly enhanced transactional convenience while expanding commercial boundaries. I firmly believe this shift is positive as it creates unprecedented opportunities for both businesses and individuals.***While traditional cash limits transactions to local merchants, digital currency enables effortless global commerce. Consider multinational corporations in Asia requiring daily transfers of millions to European partners. Physical cash transportation would be impractical, but through secure platforms like VISA, such complex transactions conclude within seconds. This efficiency not only optimizes operational processes but also fuels international trade in our globalized economy.***Furthermore, digital transactions empower individual consumers. The instantaneous nature of online payments, coupled with robust security measures, facilitates seamless e-commerce experiences. Users can confidently purchase specialized products from overseas vendors—opportunities unimaginable in the cash-dominant era. Unlike physical currency that restricts shopping to neighborhood stores, digital systems provide access to a global marketplace, dramatically enriching consumer choices.***The transition to cashless systems ultimately fosters economic connectivity on an unprecedented scale. By eliminating geographical constraints and ensuring transaction reliability, modern payment methods lay the foundation for a more integrated world economy, benefiting enterprises and consumers alike through enhanced accessibility and operational efficiency. (229 words)  \
                注意： 仅评价“写作答案”，你的评分和改进措施不应该包含{nameA}和{nameB}的回答！"
    
    user_prompt = f"请用刚才的标准评分，不要考虑{nameA}和{nameB}的回答,题目信息:'{toEvaluateProblem}'题目结束, 写作答案:'{toEvaluateAnswer}'写作答案结束，示例答案,评分不要考虑示例答案！！！，只针对前面的写作答案,官方评分28-30，仅参考内容，实际写作中可以有不同的展开思路:{extract_answer_from_file('static/table/2023_AcaTalk_Answer.txt')[question_num]}"
    debug_mode = False
    doGenerateReport = True
    if 'debug:True' in toEvaluateAnswer:
        debug_mode = True


    if not debug_mode:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": system_prompt
                },
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )

        extractedAiResponse = response.choices[0].message.content
        extractedAiResponse = extractedAiResponse.replace("***","\n<br/>\n",-1)

        entryList = extractedAiResponse.split('@@@') 
        entryList = calculate_score(entryList) + entryList
        entryList = entryList + [generateReport(*entryList,toEvaluateAnswer,question_num)]
        # for i in entryList:
        #     print(i)
        return jsonify(entryList)
    else:
        extractedAiResponse = "4.0@@@3.8@@@3.5@@@3.8@@@1. 未直接回应教授问题的'positive/negative'核心框架***2. 企业案例与个人网购的衔接不够紧密@@@1. 企业案例缺少对'效率提升'的具体解释***2. 个人网购段落缺乏对'安全保障'的展开@@@1. 拼写错误：internat→internet***2. 重复词：definitely(3次)→certainly/unquestionably***3. 基础词：good→commodity/product***4. 简单词：make→facilitate/enable@@@1. 段落间过渡生硬***2. 结论缺乏分论点总结@@@A. 在首段明确立场'This is undoubtedly positive'***B. 增加过渡句'While corporate benefits are evident, individuals also gain...'@@@B. 解释'跨国支付如何缩短交易时间'***说明'支付安全如何防止欺诈'@@@C. 错误修正：***1. evlution→evolution***2. boarder→boundaries***3. perchase→purchase***4. sonsiderably→considerably***替换建议：***1. definately→undoubtedly/certainly***2. payment→transaction/digital currency***3. improve→enhance/optimize***4. range→spectrum/diversity@@@D. 添加连接词'Furthermore/Moreover'***结论总结分论点'global accessibility and personal convenience'@@@In the internet era, the evolution of payment systems has undoubtedly enhanced transactional convenience while expanding commercial boundaries. I firmly believe this shift is positive as it creates unprecedented opportunities for both businesses and individuals.***While traditional cash limits transactions to local merchants, digital currency enables effortless global commerce. Consider multinational corporations in Asia requiring daily transfers of millions to European partners. Physical cash transportation would be impractical, but through secure platforms like VISA, such complex transactions conclude within seconds. This efficiency not only optimizes operational processes but also fuels international trade in our globalized economy.***Furthermore, digital transactions empower individual consumers. The instantaneous nature of online payments, coupled with robust security measures, facilitates seamless e-commerce experiences. Users can confidently purchase specialized products from overseas vendors—opportunities unimaginable in the cash-dominant era. Unlike physical currency that restricts shopping to neighborhood stores, digital systems provide access to a global marketplace, dramatically enriching consumer choices.***The transition to cashless systems ultimately fosters economic connectivity on an unprecedented scale. By eliminating geographical constraints and ensuring transaction reliability, modern payment methods lay the foundation for a more integrated world economy, benefiting enterprises and consumers alike through enhanced accessibility and operational efficiency. (229 words)" 
        extractedAiResponse = extractedAiResponse.replace("***","\n<br/>\n",-1)
        entryList = extractedAiResponse.split('@@@')
        entryList = calculate_score(entryList) + entryList
        entryList = entryList + [generateReport(*entryList,toEvaluateAnswer,question_num)]
        print(entryList)
        return jsonify(entryList)

    

if __name__ == '__main__':
    app.run(debug=True)
