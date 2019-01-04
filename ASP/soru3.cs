public static OleDbConnection GetConnection()
{
    OleDbConnection conn = new OleDbConnection();
    try
    {
        String connectionString = @"Provider=Microsoft.JET.OlEDB.4.0;"
        + @"Data Source=C:\örnek.mdb";
        conn = new OleDbConnection(connectionString);
        conn.Open();
    }
    catch (Exception e)
    {
        Console.WriteLine(e.Message);
    }
    return conn;
}

public static List<Kisi> KisileriListele(String sehir)
{
    List<Kisi> kisiList = new List<Kisi>();
    DataSet ds = new DataSet();
    OleDbConnection conn = GetConnection();
    String q = @"SELECT * FROM Kisiler WHERE sehir = '" + sehir + "'";
    OleDbDataAdapter da = new OleDbDataAdapter(q, conn);
    da.Fill(ds);
    conn.Close();
    DataTable dt = ds.Tables[0];
    foreach (DataRow rows in dt.Rows)
    {
        Kisi kisi = new Kisi();
        kisi.isim = rows["isim"].toString();
        kisi.soyad = rows["soyad"].toString();
        kisi.sehir = rows["sehir"].toString();
        kisi.kimlik = rows["Kimlik"].toString();
        kisiList.Add(kisi);
    }
    return kisiList;
}

public static void kisiEkle(Kisi kisi, string sessionId)
{
    OleDbConnection conn = GetConnection();
    String q = @"INSERT INTO Kisiler(isim, soyad, sehir, Kimlik, SessionId)
    VALUES(" + kisi.isim + ",'" + kisi.soyad + "',"+ kisi.sehir + ",'" + kisi.Kimlik + "','"
                + sessionId + "')";
    OleDbCommand command = new OleDbCommand(q, conn);            
    command.ExecuteNonQuery();
    conn.Close();
}

public static void kisiSil(Int64 index, string sessionId)
{
    OleDbConnection conn = GetConnection();
    String q = @"DELETE FROM Kisiler WHERE Id = " + index + " and SessionId = '" + sessionId +"'";
    OleDbCommand command = new OleDbCommand(q, conn);
    command.ExecuteNonQuery();
    conn.Close();
}

public static void kisiGuncelle(Int64 index, Kisi kisi)
{
    OleDbConnection conn = getConnection();
    String q = @"UPDATE Kisiler SET isim = '" + kisi.isim + "'" + ", soyad = '" + kisi.soyad + "', sehir = '" + kisi.sehir + "', kisi.Kimlik = '" + kisi.kimlik + "' WHERE Id = " + index + " and SessionId = '" + sessionId + "'";
    OleDbCommand command = new OleDbCommand(q, conn);
    command.ExecuteNonQuery();
    conn.Close();
}