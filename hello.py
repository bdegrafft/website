from flask import Flask, render_template, request
app = Flask(__name__)
def getContent(page,col) :
    if page == "main":
        if col == "right":
            return ["I'm a techophile living in Vermont. I've dabbled in everything from routing and switching to full stack web development. A serious penchant for philosophy, art and podcasts keeps me curious and ready for whatever's next."]
        if col == "left":
            return ["This","is","the","left","column"]
@app.route("/")
def nomic( ):
    cubesRight= getContent("main","right")
    cubesLeft= getContent("main","left")
    return render_template('nomic.html',cubesRight=cubesRight,cubesLeft=cubesLeft)
@app.route("/art")
def art():
    render_template('art.html')
if __name__ == "__main__":
    app.run(debug=True)
