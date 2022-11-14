from flask import Flask
from flask_graphql import GraphQLView
from schema import schema



app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True # for having the GraphiQL interface
    )
)


@app.route('/obj')
def showmw():
    return 'Data here'

if __name__ == '__main__':
     app.run(debug=True, port=5051, host='0.0.0.0')