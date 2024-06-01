Write a method in C# that takes a byte array as input, sends it to a database server, and returns a DataTableReader object containing the result of the query.

    Only return the code, don't include any other information,
    such as a preamble or suffix.
    */
namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] vals = new int[3];

            for (int i = 0; i < 3; ++i)
                vals[i] = i;

            byte[] bytes = BitConverter.GetBytes(vals);

            DataTableReader dataTableReader = SendDataToDatabaseServer();
        }
    }

    class DatabaseConnector
    {
        public static DataTableReader SendDataToDatabaseServer()
        {
            return null; // To be implemented by the learner
        }
    }
}
\end{code}

I can't figure out how to write the method.  I feel like this is a simple exercise, but it just doesn't click in my head for some reason.  Can someone explain how to do this?

Comment: Just to be clear what you want us to do - you have an object that does something and you want us to write the implementation of that function? Is there any particular database API we should use or is it up to you? Any other functions need to be implemented for this? What does your database schema look like?

Comment: I would suggest looking at how LINQ does its queries in EF. I'm sure that you can create an example with LINQ to SQL/ORMs and then port to whatever database you are using.

Answer: \begin{code}
namespace ConsoleApplication1
{
    class DatabaseConnector
    {
        private readonly string _databaseConnectionString;

        public DatabaseConnector(string connectionString) : this()
        {
            _databaseConnectionString = connectionString;
        }

        public static DataTableReader SendDataToDatabaseServer()
        {
            return new SqlDataAdapter().GetDataTable(new SqlCommand("..."));
        }
    }
}
\end{code}