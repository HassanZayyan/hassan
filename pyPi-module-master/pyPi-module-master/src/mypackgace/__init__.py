import requests

def get_quote():
    # API endpoint untuk mendapatkan kutipan
    endpoint = "https://api.quotable.io/random"

    try:
        # Mengirim permintaan GET ke API
        response = requests.get(endpoint)

        # Memeriksa apakah permintaan berhasil (status code 200)
        if response.status_code == 200:
            # Mengambil data JSON dari respons
            data = response.json()

            # Menampilkan kutipan dan penulisnya
            print(f"Kutipan: {data['content']}")
            print(f"Penulis: {data['author']}")
        else:
            print(f"Gagal mendapatkan kutipan. Kode status: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    # Memanggil fungsi untuk mendapatkan dan menampilkan kutipan
    get_quote()
