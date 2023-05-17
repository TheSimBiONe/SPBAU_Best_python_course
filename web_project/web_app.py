import flask
from flask import Flask, request
from parallel_boost import monte_carlo, build_plot


app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return flask.render_template(
            'base.html')
    elif request.method == 'POST':

        try:
            result = monte_carlo(request.form.get('func'),
                                 int(request.form.get('points')),
                                 tuple(map(float, request.form.get('x_limits').split())),
                                 tuple(map(float, request.form.get('y_limits').split())))

            build_plot(request.form.get('func'),
                       tuple(map(float, request.form.get('x_limits').split())),
                       *result[1:])

        except Exception:
            return flask.render_template(
                'error.html',
                func=request.form.get('func'),
                points=request.form.get('points'),
                x_limits=request.form.get('x_limits'),
                y_limits=request.form.get('y_limits'),
                method=request.method
            )

        return flask.render_template(
            'index.html',
            func=request.form.get('func'),
            points=request.form.get('points'),
            x_limits=request.form.get('x_limits'),
            y_limits=request.form.get('y_limits'),
            value=result[0],
            method=request.method)


if __name__ == '__main__':
    app.run(debug=True)
