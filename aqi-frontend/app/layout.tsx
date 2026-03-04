import "./globals.css";

export const metadata = {
  title: "AQI Dashboard",
  description: "Air Quality Monitor"
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}