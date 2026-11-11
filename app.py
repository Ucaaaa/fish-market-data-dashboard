from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "fish.csv"

app = Flask(__name__)

# Memuat dan membersihkan dataset satu kali saat aplikasi dijalankan.
df = pd.read_csv(DATA_PATH)
required_columns = {
    "Species", "Weight", "Length1", "Length2", "Length3", "Height", "Width"
}
missing_columns = required_columns.difference(df.columns)
if missing_columns:
    raise ValueError(
        "Kolom dataset tidak lengkap: " + ", ".join(sorted(missing_columns))
    )

df = df.dropna(subset=list(required_columns)).copy()
species_list = sorted(df["Species"].astype(str).unique().tolist())


def filter_data():
    """Mengambil seluruh data atau data dari spesies yang dipilih."""
    species = request.args.get("species", "").strip()
    if species and species in species_list:
        return df[df["Species"].astype(str) == species]
    return df


@app.route("/")
def dashboard():
    return render_template("dashboard.html", species_list=species_list)


@app.route("/api/ringkasan")
def ringkasan():
    data = filter_data()
    if data.empty:
        return jsonify(
            total_ikan=0,
            jumlah_spesies=0,
            rata_berat=0,
            berat_maksimum=0
        )

    return jsonify(
        total_ikan=int(len(data)),
        jumlah_spesies=int(data["Species"].nunique()),
        rata_berat=round(float(data["Weight"].mean()), 2),
        berat_maksimum=round(float(data["Weight"].max()), 2)
    )


@app.route("/api/berat-spesies")
def berat_spesies():
    data = filter_data()
    hasil = data.groupby("Species")["Weight"].mean().round(2)
    return jsonify(labels=hasil.index.tolist(), data=hasil.tolist())


@app.route("/api/panjang-berat")
def panjang_berat():
    data = filter_data()
    datasets = []
    for species, kelompok in data.groupby("Species"):
        datasets.append({
            "label": str(species),
            "data": [
                {"x": float(row["Length1"]), "y": float(row["Weight"])}
                for _, row in kelompok.iterrows()
            ]
        })
    return jsonify(datasets=datasets)


@app.route("/api/ukuran-ikan")
def ukuran_ikan():
    data = filter_data()
    kolom = ["Length1", "Length2", "Length3", "Height", "Width"]
    hasil = data.groupby("Species")[kolom].mean().round(2)

    return jsonify(
        labels=hasil.index.tolist(),
        datasets=[
            {
                "label": kolom_ukuran,
                "data": hasil[kolom_ukuran].tolist()
            }
            for kolom_ukuran in kolom
        ]
    )


if __name__ == "__main__":
    # Debug aktif hanya untuk pengembangan lokal.
    app.run(debug=True)
