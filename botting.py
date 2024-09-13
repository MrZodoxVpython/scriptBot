import socket

def bot():
    # Membuat socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Binding ke localhost dan port 12345
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Bot sedang menunggu client untuk terhubung...")

    # Terima koneksi dari client
    conn, addr = server_socket.accept()
    print(f"Terhubung dengan {addr}")

    # Percakapan
    while True:
        # Menerima pesan dari client
        data = conn.recv(1024).decode('utf-8')
        if not data or data.lower() == 'keluar':
            print("Client telah keluar.")
            break

        print(f"Client: {data}")

        # Balasan otomatis dari bot
        if "halo" in data.lower():
            response = "Bot: Halo, ada yang bisa saya bantu?"
        elif "apa kabar" in data.lower():
            response = "Bot: Saya baik, bagaimana dengan Anda?"
        else:
            response = "Bot: Maaf, saya tidak mengerti."

        # Kirimkan balasan ke client
        conn.send(response.encode('utf-8'))

    conn.close()
    print("Koneksi ditutup.")

# Memulai bot
bot()
