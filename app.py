from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas as pd
import os
from apyori import apriori

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['dataset']
        support = float(request.form['support'])
        confidence = float(request.form['confidence'])
        lift = float(request.form['lift'])

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            transactions = []
            with open(file_path, 'r') as f:
                for line in f:
                    items = [item.strip() for item in line.strip().split(',') if item.strip()]
                    if items:
                        transactions.append(items)


            rules = apriori(transactions=transactions, min_support=support, 
                            min_confidence=confidence, min_lift=lift, 
                            min_length=2, max_length=2)
            results = list(rules)

            if not results:
                return render_template('index.html', message="No rules found. Recheck your support, confidence, and lift values.")

            def inspect(results):
                lhs = [tuple(result.ordered_statistics[0].items_base)[0] for result in results]
                rhs = [tuple(result.ordered_statistics[0].items_add)[0] for result in results]
                supports = [result.support for result in results]
                confidences = [result.ordered_statistics[0].confidence for result in results]
                lifts = [result.ordered_statistics[0].lift for result in results]
                return list(zip(lhs, rhs, supports, confidences, lifts))

            results_df = pd.DataFrame(inspect(results), 
                                      columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
            results_df = results_df.sort_values(by='Lift', ascending=False)
            result_path = os.path.join(RESULT_FOLDER, 'association_rules.csv')
            results_df.to_csv(result_path, index=False)
            return render_template('index.html', tables=[results_df.to_html(classes='table table-bordered', index=False)], download=True)

    return render_template('index.html')

@app.route('/download')
def download():
    path = os.path.join(RESULT_FOLDER, 'association_rules.csv')
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


