from flask import Flask, render_template, request, jsonify
from main import ice_breaker

app=Flask(__name__)

@app.route("/process", methods=['POST'])
def process():
    name =request.form['name']
    person_info, profile_pic_url=ice_breaker(name=name)


    return jsonify({"summary":person_info.summary,
                    "interests":person_info.topics_of_interest,
                    "facts":person_info.facts,
                    "ice_breaker":person_info.ice_breakers,
                    "profile_picture":profile_pic_url})


if __name__=="main":
    app.run(host="0.0.0.0", debug=True)
