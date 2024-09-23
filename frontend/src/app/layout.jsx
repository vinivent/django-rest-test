import "./globals.css";
import { Inter } from "next/font/google";
import Navbar from "@/components/Navbar";
import ToastProvider from "@/lib/react-toastify/ToastProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Meu App",
  description: "App com Toastify",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <ToastProvider>
          <Navbar />
          {children}
        </ToastProvider>
      </body>
    </html>
  );
}
