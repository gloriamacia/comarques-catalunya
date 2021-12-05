from flask import Flask, render_template, url_for
import folium

app = Flask(__name__)

@app.route("/")
def index():
    # https://stackoverflow.com/questions/37379374/insert-the-folium-maps-into-the-jinja-template
    start_coords = (41.3874, 2.1686)
    folium_map = folium.Map(location=start_coords, zoom_start=14, width="100%", height="100%")
    folium_map.save('templates/map.html')
    return render_template('index.html', folium_map=folium_map._repr_html_())


if __name__ == '__main__':
    app.run(debug=True)
