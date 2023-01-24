
from bottle import Bottle, template, request

app = Bottle()

@app.route('/create_palette')
def create_palette():
    hex_codes = request.query.hex_codes
    hex_list = hex_codes.split(',')
    return template('palette', hex_codes=hex_list)

@app.route('/')
def index():
    return '''
        <form action="/create_palette" method="get">
            <input type="text" name="hex_codes" placeholder="Enter hex codes separated by commas" />
            <input type="submit" value="Create Palette">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
