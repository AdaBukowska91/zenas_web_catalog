import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select COLOR_OR_STYLE from CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)

