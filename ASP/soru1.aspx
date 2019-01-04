<table>
  <tr>
    <td>
      Ad
    </td>
    <td>
      <asp:TextBox ID="txtAd" runat="server" />
    </td>
    <td>
      <asp:RequiredFieldValidator ErrorMessage="Zorunlu" ControlToValidate="txtAd" runat="server" />
    </td>
  </tr>
  <tr>
    <td>
      Soyad
    </td>
    <td>
      <asp:TextBox ID="txtSoyad" runat="server" />
    </td>
    <td>
      <asp:RequiredFieldValidator ErrorMessage="Zorunlu" ControlToValidate="txtSoyad" runat="server" />
    </td>
  </tr>
  <tr>
    <td>
      Kullanici Adi
    </td>
    <td>
        <asp:TextBox ID="txtKullaniciAdi" runat="server" />
    </td>
    <td>
      <asp:RequiredFieldValidator ErrorMessage="Zorunlu" ControlToValidate="txtKullaniciAdi" runat="server" />
    </td>  
  </tr>
  <tr>
        <td>
            Sifre
        </td>
        <td>
            <asp:TextBox ID="txtSifre" runat="server" TextMode="Password" />
        </td>
        <td>
            <asp:RegularExpressionValidator ErrorMessage="Sifre 5 haneli bir sayi olmalidir" ValidationExpression="\d{5}" ControlToValidate="txtSifre" runat="server" />
            <asp:RequiredFieldValidator ErrorMessage="Required" ControlToValidate="txtSifre" runat="server" />
        </td>
    </tr>
    <tr>
        <td>
            Sifre Tekrar
        </td>
        <td>
            <asp:TextBox ID="txtSifreTekrar" runat="server" TextMode="Password" />
        </td>
        <td>
            <asp:CompareValidator ErrorMessage="Sifreler ayni degil." ControlToCompare="txtSifreTekrar" ControlToValidate="txtSifre" runat="server" />
        </td>
    </tr>
        <tr>
        <td>
            <asp:Button Text="Kaydol" runat="server" OnClick="Kaydol" />
        </td>
    </tr>
</table>
