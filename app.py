from flask import Flask, render_template, request

app = Flask(__name__)

#percorso per la pagina principale
@app.route('/')
def index():
    return render_template('index.html')

#percorso per il calcolo del valore
@app.route('/calcola', methods=['POST'])
def calcola():
    #prendo i dati dal form
    mq = float(request.form['metri_quadri'])
    prezzo_mq = float(request.form['prezzo_mq'])
    stato = request.form['stato']
    vista_mare = request.form['vista']
    parcheggio = request.form['parcheggio']
    giardino = request.form['giardino']

    #calcolo i valori
    valore = mq * prezzo_mq

    if stato == 'Nuovo':
        valore *= 1.2
    elif stato == 'Medio':
        valore *= 1.0
    elif stato == 'Da ristrutturare':
        valore *= 0.8

    if vista_mare == 'Completa':
        valore *= 1.17
    elif vista_mare == 'Parziale':
        valore *= 1.08

    if parcheggio == 'Riservato':
        valore *= 1.05
    elif parcheggio == 'Box':
        valore *= 1.15

    if giardino == 'Presente':
        valore *= 1.08

    #arrotondo il valore sulla linea delle centinaia
    valore = round(valore / 1000) * 1000

    #mando il valore alla pagina risultato
    return render_template('result.html', valore=valore)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)




    
    