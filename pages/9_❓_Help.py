import streamlit as st


DATA_TYPES_AND_COLUMNS = """

### Columns

| Column Name | Description |
| ----------- | ----------- |
| `Activity Type`   | |
|                   | <blank> |
|                   | S - 'signal' |
|                   | M - 'message' |
|                   | C - 'comms (between dispatchers?)' |
| `Apparatus Status` | |
|                   | <blank> |
|                   | DP - 'dispatched' |
|                   | EN - 'enroute' |
|                   | OS - 'on scene' |
|                   | OG - 'staged' |
|                   | TR - 'transporting' |
|                   | TC - 'transport complete' |
|                   | AV - 'available' |
|                   | IQ - 'in quarters' |
|                   | ZZ - 'no status but on board' |
|                   | FF - 'Crew members riding in to hopital with AMR' |
|                   | NA - 'OOS with code' |
| `Activity Code`   | |
|                  | <blank> |
|                  | CM - ??? |
|                  | 7P - 'personnel (AMR lunch break taken at end of shift)' |
|                  | 7C - 'AMR Company Code 1 (aka private transport)' |
|                  | 90 - ?? |
|                  | 91 - ?? |
|                  | 98 - ?? |
|                  | 99 - ?? |

"""



# with st.expander("How to export data from 'remote CAD'"):
#     image_column, text_column = st.columns ( (1, 2) )

#     with image_column:
#         st.image("https://picsum.photos/200")
    
#     with text_column:
#         st.write("This is a column of text")


st.header("Exporting data from Remote CAD", divider="rainbow")
st.write(DATA_TYPES_AND_COLUMNS)
