import java.sql.*;

public class RelationalDatabaseDemo {

    /* Basic function to test connection to database */
    public static boolean testConnection(Connection conn){
        try {
            return !conn.isClosed();
        }
        catch (Exception ex) {
            return false;
        }
    }

    /* This function lists the tables in the current database (database schema) */
    public static void listDatabaseSchema(Connection conn){
        try{
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SHOW TABLES;");
            System.out.println("Tables in current database:");
            while (rs.next()){
                System.out.println(rs.getString(1));
            }
        }
        catch (Exception ex){
            System.out.println("This operation could not be completed");
        }
    }

    /* This function lists the data in the specified table */
    public static void listDataInTable(String tableName, Connection conn){
        try{
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(String.format("SELECT * FROM %s;", tableName));

            ResultSetMetaData rsmd = rs.getMetaData();
            int columnCount = rsmd.getColumnCount();

            System.out.println(String.format("Records in table %s:", tableName));
            while (rs.next()){
                for (int i = 1; i <= columnCount; i++)
                    System.out.print(rs.getString(i) + " ");
                System.out.println();
            }
        }
        catch (Exception ex){
            System.out.println("This operation could not be completed");
        }
    }



    public static void main(String [] args){

        try{
            Connection conn = DriverManager.getConnection("jdbc:mysql://(localhost=33060,user=Demo," +
                    "password=bad_password)/Demo");

            boolean isConnected = testConnection(conn);
            System.out.println(isConnected);

            listDatabaseSchema(conn);

            listDataInTable("patient", conn);

        }

        catch (SQLException ex){
            System.out.println(ex.getMessage());
        }
        catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

    }

}
