/*
 Middle East Technical University
 Computer Engineering
 2018 Fall
 CENG351 - Data Management And File Structures
 THE1 - The MUSICDB Issue
 
 ID: 2319143
 Full Name: Ersegun Omer EROL

 ALL RIGHTS RESERVED...
*/

package ceng.ceng351.musicdb;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import ceng.ceng351.musicdb.QueryResult.ArtistNameSongNameGenreRatingResult;
import ceng.ceng351.musicdb.QueryResult.ArtistNameNumberOfSongsResult;
import ceng.ceng351.musicdb.QueryResult.TitleReleaseDateRatingResult;
import ceng.ceng351.musicdb.QueryResult.UserIdUserNameNumberOfSongsResult;


public class MUSICDB implements IMUSICDB{
/*
    private static String user = "root";
    private static String password = "realove94";
    private static String host = "127.0.0.1";
    private static String database = "ersegunomer";
    private static int port = 3306;
    */
    private static String user = "e2319143";
    private static String password = "967c45b1";
    private static String host = "144.122.71.57";
    private static String database = "db2319143";
    private static int port = 8084;

    private Connection con;

    @Override
    public void initialize() {
        String url = "jdbc:mysql://" + this.host + ":" + this.port + "/" + this.database;

        try {
            Class.forName("com.mysql.jdbc.Driver");
            this.con =  DriverManager.getConnection(url, this.user, this.password);
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    @Override
    public int createTables() {

        int us,so,ar,al,li;
        int numberofTablesInserted = 0;

        // !!! NOT NULL etc. WILL BE CHECKED !!!


        /* Recit. Ex.
        String queryCreatePlayerTable = "create table Player (" +
                "number int not null," +
                "teamname char(20) not null," +
                "name char(30)," +
                "age int," +
                "position char(3)," +
                "primary key (number,teamName))";
        */


        //user(userID:int, userName:varchar(60), email:varchar(30), password:varchar(30))
        String queryCREATETABLEuser = "CREATE TABLE user (" +
                "userID int NOT NULL," +
                "userName varchar(60)," +
                "email varchar(30)," +
                "password varchar(30)," +
                "PRIMARY KEY (userID))";

        //artist(artistID:int, artistName:varchar(60))
        String queryCREATETABLEartist = "CREATE TABLE artist (" +
                "artistID int NOT NULL," +
                "artistName varchar(60)," +
                "PRIMARY KEY (artistID))";

        //album(albumID:int, title:varchar(60), albumGenre:varchar(30), albumRating:double, releaseDate:date, artistID:int)
        String queryCREATETABLEalbum = "CREATE TABLE album (" +
                "albumID int NOT NULL," +
                "title varchar(60)," +
                "albumGenre varchar(30)," +
                "albumRating double," +
                "releaseDate date," +
                "artistID int," +
                "PRIMARY KEY (albumID)," +
                "FOREIGN KEY (artistID) REFERENCES artist(artistID) ON UPDATE CASCADE ON DELETE CASCADE)";

        //song(songID:int, songName:varchar(60), genre:varchar(30), rating:double, artistID:int, albumID:int)
        String queryCREATETABLEsong = "CREATE TABLE song (" +
                "songID int NOT NULL," +
                "songName varchar(60)," +
                "genre varchar(30)," +
                "rating double," +
                "artistID int," +
                "albumID int," +
                "PRIMARY KEY (songID)," +
                "FOREIGN KEY (artistID) REFERENCES artist(artistID) ON UPDATE CASCADE ON DELETE CASCADE," +
                "FOREIGN KEY (albumID) REFERENCES album(albumID) ON UPDATE CASCADE ON DELETE CASCADE)";

        //listen(userID:int, songID:int, lastListenTime:timestamp, listenCount:int)
        String queryCREATETABLElisten = "CREATE TABLE listen (" +
                "userID int NOT NULL," +
                "songID int NOT NULL," +
                "lastListenTime timestamp," +
                "listenCount int," +
                "PRIMARY KEY (userID,songID)," +
                "FOREIGN KEY (userID) REFERENCES user(userID) ON UPDATE CASCADE ON DELETE CASCADE," +
                "FOREIGN KEY (songID) REFERENCES song(songID) ON UPDATE CASCADE ON DELETE CASCADE)";

        try {
            Statement statement = this.con.createStatement();

            //user
            us = statement.executeUpdate(queryCREATETABLEuser);
            //System.out.println(us + "user");
            numberofTablesInserted++;

            //artist
            ar = statement.executeUpdate(queryCREATETABLEartist);
            //System.out.println(ar + "artist");
            numberofTablesInserted++;

            //album
            al = statement.executeUpdate(queryCREATETABLEalbum);
            //System.out.println(al + "album");
            numberofTablesInserted++;

            //song
            so = statement.executeUpdate(queryCREATETABLEsong);
            //System.out.println(so + "song");
            numberofTablesInserted++;

            //listen
            li = statement.executeUpdate(queryCREATETABLElisten);
            //System.out.println(li + "listen");
            numberofTablesInserted++;

            //close
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return numberofTablesInserted;
    }

    @Override
    public int dropTables() {
        int us,so,ar,al,li;
        int numberofTablesDropped = 0;

        //listen(userID:int, songID:int, lastListenTime:timestamp, listenCount:int)
        String queryDROPTABLElisten = "DROP TABLE if EXISTS listen";

        //song(songID:int, songName:varchar(60), genre:varchar(30), rating:double, artistID:int, albumID:int)
        String queryDROPTABLEsong = "DROP TABLE if EXISTS song";

        //album(albumID:int, title:varchar(60), albumGenre:varchar(30), albumRating:double, releaseDate:date, artistID:int)
        String queryDROPTABLEalbum = "DROP TABLE if EXISTS album";

        //artist(artistID:int, artistName:varchar(60))
        String queryDROPTABLEartist = "DROP TABLE if EXISTS artist";

        //user(userID:int, userName:varchar(60), email:varchar(30), password:varchar(30))
        String queryDROPTABLEuser = "DROP TABLE if EXISTS user";

        try {
            Statement statement = this.con.createStatement();

            //listen
            li = statement.executeUpdate(queryDROPTABLElisten);
            //System.out.println(li);
            numberofTablesDropped++;

            //song
            so = statement.executeUpdate(queryDROPTABLEsong);
            //System.out.println(so);
            numberofTablesDropped++;

            //album
            al = statement.executeUpdate(queryDROPTABLEalbum);
            //System.out.println(al);
            numberofTablesDropped++;

            //artist
            ar = statement.executeUpdate(queryDROPTABLEartist);
            //System.out.println(ar);
            numberofTablesDropped++;

            //user
            us = statement.executeUpdate(queryDROPTABLEuser);
            //System.out.println(us);
            numberofTablesDropped++;

            //close
            statement.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return numberofTablesDropped;
    }

    @Override
    public int insertAlbum(Album[] albums) {
        int result = 0;
        int numberofRowsInsertedSuccesfully = 0;

        //album(albumID:int, title:varchar(60), albumGenre:varchar(30), albumRating:double, releaseDate:date, artistID:int)
        for(int i=0; i < albums.length; i++) {
            String modified_title = albums[i].getTitle().replace("'", " ");
            String query = "INSERT INTO album VALUES ('" +
                    albums[i].getAlbumID() + "','" +
                    modified_title + "','" +
                    albums[i].getAlbumGenre() + "','" +
                    albums[i].getAlbumRating() + "','" +
                    albums[i].getReleaseDate() + "','" +
                    albums[i].getArtistID() + "')";

            try {
                Statement st = this.con.createStatement();
                result = st.executeUpdate(query);
                //System.out.println(result);
                numberofRowsInsertedSuccesfully++;

                //Close
                st.close();

            } catch (SQLException e) {
                e.printStackTrace();
                //if (e.toString().contains("SQLIntegrityConstraintViolationException")){
                //    throw new AlreadyInsertedException();
                //}
            }
        }
        return numberofRowsInsertedSuccesfully;
    }

    @Override
    public int insertArtist(Artist[] artists) {
        int result = 0;
        int numberofRowsInsertedSuccesfully = 0;

        //artist(artistID:int, artistName:varchar(60))
        for(int i=0; i < artists.length; i++) {
            String query = "INSERT INTO artist VALUES ('" +
                    artists[i].getArtistID() + "','" +
                    artists[i].getArtistName() + "')";

            try {
                Statement st = this.con.createStatement();
                result = st.executeUpdate(query);
                //System.out.println(result);
                numberofRowsInsertedSuccesfully++;

                //Close
                st.close();

            } catch (SQLException e) {
                e.printStackTrace();
                //if (e.toString().contains("SQLIntegrityConstraintViolationException")){
                //    throw new AlreadyInsertedException();
                //}
            }
        }
        return numberofRowsInsertedSuccesfully;
    }

    @Override
    public int insertSong(Song[] songs) {
        int result = 0;
        int numberofRowsInsertedSuccesfully = 0;

        //song(songID:int, songName:varchar(60), genre:varchar(30), rating:double, artistID:int, albumID:int)
        for(int i=0; i < songs.length; i++) {
            String modified_songName = songs[i].getSongName().replace("'", " ");
            String query = "INSERT INTO song VALUES ('" +
                    songs[i].getSongID() + "','" +
                    modified_songName + "','" +
                    songs[i].getGenre() + "','" +
                    songs[i].getRating() + "','" +
                    songs[i].getArtistID() + "','" +
                    songs[i].getAlbumID() + "')";

            try {
                Statement st = this.con.createStatement();
                result = st.executeUpdate(query);
                //System.out.println(result);
                numberofRowsInsertedSuccesfully++;

                //Close
                st.close();

            } catch (SQLException e) {
                e.printStackTrace();
                //if (e.toString().contains("SQLIntegrityConstraintViolationException")){
                //    throw new AlreadyInsertedException();
                //}
            }
        }
        return numberofRowsInsertedSuccesfully;
    }

    @Override
    public int insertUser(User[] users) {
        int result = 0;
        int numberofRowsInsertedSuccesfully = 0;

        //user(userID:int, userName:varchar(60), email:varchar(30), password:varchar(30))
        //new user(3829, "ersgunomer", "e.omer.erol@gmail.com", "GeneralPassword01"),
        for(int i=0; i < users.length; i++) {
            String query = "INSERT INTO user VALUES ('" +
                    users[i].getUserID() + "','" +
                    users[i].getUserName() + "','" +
                    users[i].getEmail() + "','" +
                    users[i].getPassword() + "')";

            try {
                Statement st = this.con.createStatement();
                result = st.executeUpdate(query);
                //System.out.println(result);
                numberofRowsInsertedSuccesfully++;

                //Close
                st.close();

            } catch (SQLException e) {
                e.printStackTrace();
                //if (e.toString().contains("SQLIntegrityConstraintViolationException")){
                //    throw new AlreadyInsertedException();
                //}
            }
        }
        return numberofRowsInsertedSuccesfully;
    }

    @Override
    public int insertListen(Listen[] listens) {
        int result = 0;
        int numberofRowsInsertedSuccesfully = 0;

        //listen(userID:int, songID:int, lastListenTime:timestamp, listenCount:int)
        for(int i=0; i < listens.length; i++) {
            String query = "INSERT INTO listen VALUES ('" +
                    listens[i].getUserID() + "','" +
                    listens[i].getSongID() + "','" +
                    listens[i].getLastListenTime() + "','" +
                    listens[i].getListenCount() + "')";

            try {
                Statement st = this.con.createStatement();
                result = st.executeUpdate(query);
                //System.out.println(result);
                numberofRowsInsertedSuccesfully++;

                //Close
                st.close();

            } catch (SQLException e) {
                e.printStackTrace();
                //if (e.toString().contains("SQLIntegrityConstraintViolationException")){
                //    throw new AlreadyInsertedException();
                //}
            }
        }
        return numberofRowsInsertedSuccesfully;
    }

    ///////////////////////////////// *** 3.3 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public QueryResult.ArtistNameSongNameGenreRatingResult[] getHighestRatedSongs() {
        ResultSet rs;
        ArrayList<ArtistNameSongNameGenreRatingResult> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT ar.artistName, so.songName, so.genre, so.rating " +
                        "FROM artist ar, song so " +
                        "WHERE ar.artistID = so.artistID AND so.rating >= ALL (SELECT so2.rating FROM song so2) " +
                        "ORDER BY ar.artistName ASC;";

        //System.out.println("3.3 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next()){
                String artistName = rs.getString(1);
                String songName = rs.getString(2);
                String genre = rs.getString(3);
                double rating = rs.getDouble(4);
                MyResultList.add(new QueryResult.ArtistNameSongNameGenreRatingResult(artistName, songName, genre, rating));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new QueryResult.ArtistNameSongNameGenreRatingResult[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.4 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public QueryResult.TitleReleaseDateRatingResult getMostRecentAlbum(String artistName) {
        ResultSet rs;
        String MyValue = artistName;
        QueryResult.TitleReleaseDateRatingResult MyResult = null;
        String query = "SELECT DISTINCT al.title, al.releaseDate, al.albumRating" +
                        " FROM album al, artist ar" +
                        " WHERE ar.artistName = '" + MyValue + "' AND al.artistID = ar.artistID" +
                        " AND al.releaseDate >= ALL(SELECT al2.releaseDate FROM album al2);";

        //System.out.println("3.4 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);

            rs.next();
            MyResult = new QueryResult.TitleReleaseDateRatingResult(rs.getString("title"), rs.getString("releaseDate"), rs.getDouble("albumRating"));


            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResult;
    }

    ///////////////////////////////// *** 3.5 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public QueryResult.ArtistNameSongNameGenreRatingResult[] getCommonSongs(String userName1, String userName2) {
        ResultSet rs;
        String My1stUser = userName1;
        String My2ndUser = userName2;
        ArrayList<ArtistNameSongNameGenreRatingResult> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT ar.artistName, so.songName, so.genre, so.rating" +
                        " FROM artist ar, song so, listen li1, user us1, listen li2, user us2" +
                        " WHERE us1.userID = li1.userID AND us2.userID = li2.userID AND li1.songID = so.songID" +
                        " AND li2.songID = so.songID AND so.artistID = ar.artistID" +
                        " AND us1.userName = '" + My1stUser + "' AND us2.userName = '" + My2ndUser +
                        "' ORDER BY so.rating DESC;";

        //System.out.println("3.5 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next()){
                String artistName = rs.getString(1);
                String songName = rs.getString(2);
                String genre = rs.getString(3);
                double rating = rs.getDouble(4);
                MyResultList.add(new QueryResult.ArtistNameSongNameGenreRatingResult(artistName, songName, genre, rating));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new QueryResult.ArtistNameSongNameGenreRatingResult[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.6 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public QueryResult.ArtistNameNumberOfSongsResult[] getNumberOfTimesSongsListenedByUser(String userName) {
        ResultSet rs;
        String MyUser = userName;
        ArrayList<ArtistNameNumberOfSongsResult> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT ar.artistName, SUM(li.listenCount)" +
                        " FROM user us, artist ar, listen li, song so" +
                        " WHERE us.userName = '" + MyUser + "' AND us.userID = li.userID" +
                        " AND li.songID = so.songID AND so.artistID = ar.artistID" +
                        " GROUP BY ar.artistName" +
                        " ORDER BY ar.artistName ASC;";

        //System.out.println("3.6 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next())
            {
                String artistName = rs.getString(1);
                int total = rs.getInt(2);
                MyResultList.add(new QueryResult.ArtistNameNumberOfSongsResult(artistName, total));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new QueryResult.ArtistNameNumberOfSongsResult[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.7 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public User[] getUsersWhoListenedAllSongs(String artistName) {
        ResultSet rs;
        String MyArtist = artistName;
        ArrayList<User> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT us.userID, us.userName, us.email, us.password" +
        " FROM user us" +
        " WHERE NOT EXISTS (SELECT * FROM song so, artist ar" +
                " WHERE ar.artistName = '" + MyArtist +"' AND ar.artistID = so.artistID" +
                " AND so.songID NOT IN (" +
                        " SELECT li.songID" +
                        " FROM listen li" +
                        " WHERE us.userID = li.userID))" +
        " ORDER BY us.userID ASC;";

        //System.out.println("3.7 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next())
            {
                int userID = rs.getInt(1);
                String userName = rs.getString(2);
                String email = rs.getString(3);
                String password = rs.getString(4);
                MyResultList.add(new User(userID, userName, email, password));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new User[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.8 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public QueryResult.UserIdUserNameNumberOfSongsResult[] getUserIDUserNameNumberOfSongsNotListenedByAnyone() {
        /*
        ResultSet rs,rs2;
        int numberofUsers = 0;
        String MyCurrUser = null;
        String query = "SELECT us.userID, us.userName" +
                        " FROM user us;";
        ArrayList<UserIdUserNameNumberOfSongsResult> MyTempList = new ArrayList<>();
        ArrayList<UserIdUserNameNumberOfSongsResult> MyResultList = new ArrayList<>();


        String query2 = "SELECT us.userID, us.userName, li.listenCount"+
                        " FROM user us, listen li"+
                        " WHERE us.userID = li.userID AND us.userName = '" + MyCurrUser + "' AND li.songID NOT IN ("+
                            " SELECT li2.songID"+
                            " FROM listen li2, user us2"+
                            " WHERE us2.userName <> '" + MyCurrUser + "' AND li2.userID = us2.userID)"+
                        " ORDER BY us.userID ASC;";

        //System.out.println("3.6 OK");

        try {

            Statement st = this.con.createStatement();
            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next())
            {
                int userID = rs.getInt(1);
                String userName = rs.getString(2);
                int noneed = 0;
                MyTempList.add(new QueryResult.UserIdUserNameNumberOfSongsResult(userID, userName, noneed));
                numberofUsers++;
            }

            rs2 = st.executeQuery(query2);
            //rs.next();
            int i = 0;
            for(i=0 ; i<numberofUsers; i++)
            {
                while(rs2.next()) {
                    rs.next();
                    MyCurrUser = rs.getString(2);
                    int userID = rs2.getInt(1);
                    String userName = rs2.getString(2);
                    int listenCount = rs2.getInt(3);
                    MyResultList.add(new QueryResult.UserIdUserNameNumberOfSongsResult(userID, userName, listenCount));
                }
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new QueryResult.UserIdUserNameNumberOfSongsResult[MyResultList.size()]);
    }
*/
        return new QueryResult.UserIdUserNameNumberOfSongsResult[0];
    }
    ///////////////////////////////// *** 3.9 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public Artist[] getArtistSingingPopGreaterAverageRating(double rating) {
        ResultSet rs;
        double MyRating = rating;
        ArrayList<Artist> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT ar.artistID, ar.artistName" +
        " FROM artist ar" +
        " WHERE ar.artistID IN (" +
               " SELECT TEMP.artistID FROM(SELECT so3.artistID, AVG(so3.rating) AS averagerating" +
        " FROM song so3" +
        " GROUP BY so3.artistID" +
        " HAVING averagerating > " + MyRating + ") AS TEMP) AND ar.artistID IN (" +
                " SELECT ar2.artistID" +
        " FROM artist ar2, song so2" +
        " WHERE so2.genre = 'Pop' AND ar2.artistID = so2.artistID)" +
        " ORDER BY ar.artistID ASC;";

        //System.out.println("3.9 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next())
            {
                int artistID = rs.getInt(1);
                String artistName = rs.getString(2);
                MyResultList.add(new Artist(artistID, artistName));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new Artist[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.10 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public Song[] retrieveLowestRatedAndLeastNumberOfListenedSongs() {
        ResultSet rs;
        ArrayList<Song> MyResultList = new ArrayList<>();
        String query = "SELECT DISTINCT so.songID, so.songName, so.genre, so.rating, so.artistID, so.albumID"+
        " FROM song so"+
        " WHERE so.genre = 'Pop' AND so.rating < ANY(SELECT so2.rating FROM song so2)"+
        " AND so.songID IN (SELECT li.songID FROM listen li WHERE li.listenCount < ANY(SELECT li2.listenCount FROM listen li2))"+
        " ORDER BY so.songID ASC;";

        //System.out.println("3.10");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);
            //rs.next();
            while(rs.next())
            {
                int songID = rs.getInt(1);
                String songName = rs.getString(2);
                String genre = rs.getString(3);
                double rating = rs.getDouble(4);
                int artistID = rs.getInt(5);
                int albumID = rs.getInt(6);
                MyResultList.add(new Song(songID, songName, genre, rating, artistID, albumID));
            }

            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return MyResultList.toArray(new Song[MyResultList.size()]);
    }

    ///////////////////////////////// *** 3.11 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public int multiplyRatingOfAlbum(String releaseDate) {
        //ResultSet rs;
        String MyDate = releaseDate;
        int numberofRowsAffected = 0;
        String query = "UPDATE album" +
        " SET albumRating = albumRating * 1.5" +
        " WHERE releaseDate > '" + MyDate + "';";

        ResultSet rs2;
        String query2 = "SELECT COUNT(*)" +
                " FROM album" +
                " WHERE releaseDate > '" + MyDate + "';";

        //System.out.println("3.11 OK");

        try {

            Statement st = this.con.createStatement();

            rs2 = st.executeQuery(query2);

            rs2.next();
            int times = rs2.getInt(1);

            int i = 0;

            for(i=0; i<times; i++){
                st.executeUpdate(query);
                numberofRowsAffected++;
            }

            st.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return numberofRowsAffected;
    }

    ///////////////////////////////// *** 3.12 *** \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    @Override
    public Song deleteSong(String songName) {
        ResultSet rs;
        String MysongName = songName;
        Song song  = null;

        String query = "SELECT so.songID, so.songName, so.genre, so.rating, al.artistID, al.albumID" +
                        " FROM song so, album al" +
                        " WHERE so.albumID = al.albumID AND so.songName = '" + MysongName + "';";

        //System.out.println("3.12 OK");

        try {

            Statement st = this.con.createStatement();

            rs = st.executeQuery(query);

            rs.next();

            int songID = rs.getInt(1);
            String songName2 = rs.getString(2);
            String genre = rs.getString(3);
            double rating = rs.getDouble(4);
            int artistID = rs.getInt(5);
            int albumID = rs.getInt(6);

            song = new Song(songID, songName2, genre, rating, artistID, albumID);

            String query2 = "DELETE FROM song" +
                            " WHERE songName = '" + MysongName + "';";

            st.executeUpdate(query2);

            //Close
            st.close();


        } catch (SQLException e) {
            e.printStackTrace();
        }

        return song;
    }
}
