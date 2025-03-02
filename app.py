from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Códigos Pix fornecidos
pix_codes = {
    5: "00020126580014br.gov.bcb.pix01366e4fcd89-03b3-4b3f-becb-1530a1ee5dcf52040000530398654045.005802BR5923Rhuan Igor Licurgo Much6008Brasilia62240520daqr20147465193748146304B24A",
    10: "00020126580014br.gov.bcb.pix01366e4fcd89-03b3-4b3f-becb-1530a1ee5dcf520400005303986540510.005802BR5923Rhuan Igor Licurgo Much6008Brasilia62240520daqr201474651948932063048665",
    15: "00020126580014br.gov.bcb.pix01366e4fcd89-03b3-4b3f-becb-1530a1ee5dcf520400005303986540515.005802BR5923Rhuan Igor Licurgo Much6008Brasilia62240520daqr201474651951405663046CEE",
    20: "00020126580014br.gov.bcb.pix01366e4fcd89-03b3-4b3f-becb-1530a1ee5dcf520400005303986540520.005802BR5923Rhuan Igor Licurgo Much6008Brasilia62240520daqr201474651953735263041717",
    'outro': "00020126580014br.gov.bcb.pix01366e4fcd89-03b3-4b3f-becb-1530a1ee5dcf5204000053039865802BR5923Rhuan Igor Licurgo Much6008Brasilia62240520daqr201474651956529963047DB5"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_pix_code', methods=['POST'])
def generate_pix_code():
    value = request.json.get('value')
    if value in pix_codes:
        return jsonify({'pix_code': pix_codes[value]})
    return jsonify({'error': 'Código Pix não encontrado.'}), 404

if __name__ == "__main__":
    app.run(debug=True)
