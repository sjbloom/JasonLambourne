#Connect to sql server
$SqlConnection = New-Object System.Data.SqlClient.SqlConnection
$SqlConnection.ConnectionString = "Server=HC2012\HCLAPTOPSB;Database=EdwAdmin;Integrated Security=True" 
$SqlCmd = New-Object System.Data.SqlClient.SqlCommand
$SqlCmd.Connection = $SqlConnection
$SqlAdapter = New-Object System.Data.SqlClient.SqlDataAdapter
$DataSet = New-Object System.Data.DataSet
$SqlCmd.CommandText = "EXEC EDWADMIN.ClientAdmin.MDMActivityUpdate applicationstatus,$($SucessIndicator)"
$SqlAdapter.SelectCommand = $SqlCmd
$SqlAdapter.Fill($DataSet) #execute the sql
$SqlConnection.Close()
#$DataSet.Tables[0]
