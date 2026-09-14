# import streamlit as st
# from db_connection import create_connection
# st.title("Hospital Resource Intelligence Dashboard")

# st.write("Welcome to the Hospital Resource Intelligence System!")

# # try:
# #     connection = create_connection()

# #     if connection.is_connected():
# #         st.success("Streamlit is working!")

# #         connection.close()
 
# # except Exception as e : # Exception is Python's general error type.
# #     st.error(f"database connection failed: {e}") 

# connection = create_connection()
# cursor = connection.cursor(buffered=True)


# q1 = "SELECT DISTINCT city FROM HOSPITAL"
# cursor.execute(q1)

# cities = cursor.fetchall()

# city_names = [r[0] for r in cities]

# selected_city = st.selectbox("Selected city" , city_names)

# # %s is a placeholder for the city name
# hospital_query = """
# SELECT h_name
# FROM HOSPITAL
# WHERE city = %s 
# """
# cursor.execute(hospital_query, (selected_city,))

# hospitals = cursor.fetchall()

# hospital_names = [row[0] for row in hospitals]

# selected_hospitals = st.selectbox("Selected hospitals" , hospital_names)

# booking_type = st.radio(
#     "What do you want to book?" , ["Bed" , "Ambulance"]
# )

# if booking_type == "Bed" :
#     # st.write("You selected Bed Booking")
#     st.subheader("Bed Booking")

#     bed_query = """

#         SELECT DISTINCT b.B_type
#     FROM BEDS AS b
#     JOIN DEPARTMENT AS d
#         ON b.D_id = d.D_id
#     JOIN HOSPITAL AS h
#         ON d.h_id = h.h_id
#     WHERE h.h_name = %s
#       AND b.avilable_bed > 0
#     """

#     cursor.execute(bed_query , (selected_hospitals,))

#     bed_types = cursor.fetchall()

#     bed_types_name = [row[0] for row in bed_types]

#     selected_bed_type = st.selectbox(
#         "Select bed type", bed_types_name
#     )

#     availability_query = """
#     SELECT b.B_id, b.avilable_bed
#     FROM BEDS AS b
#     JOIN DEPARTMENT AS d
#         ON b.D_id = d.D_id
#     JOIN HOSPITAL AS h
#         ON d.h_id = h.h_id
#     WHERE h.h_name = %s
#       AND b.B_type = %s
#       AND b.avilable_bed > 0
#     ORDER BY b.B_id
# """

#     cursor.execute(availability_query, (selected_hospitals , selected_bed_type))
#     available_beds = cursor.fetchall()
#     total_available = sum(row[1] for row in available_beds)

#     if total_available > 0:
#         st.info(f"available beds :{total_available}")

#         patient_name = st.text_input("Patient name")

#         number_of_beds = st.number_input( ############################
#             "Number of beds",
#             min_value = 1 ,
#             max_value=total_available,
#             step=1
#         )

#         if st.button("Confirm Booking") :
#             if patient_name.strip() == "" :
#                 st.warning("Please Enter the Patient Name")
#             else :
#                 # st.success("Booking Details are ready!")

#                 remaining_beds = number_of_beds
#                 for b_id , available in available_beds:

#                     if remaining_beds <= 0 :
#                         break
#                     beds_to_take = min(available,remaining_beds)
#                     updated_query = """
#                         UPDATE BEDS
#                         SET avilable_bed = avilable_bed - %s
#                         WHERE B_id = %s
#                         AND avilable_bed >= %s
#                     """
#                     cursor.execute(
#                         updated_query,
#                         (beds_to_take , b_id , beds_to_take)
#                     )
#                     if cursor.rowcount != 1 :
#                         connection.rollback()
#                         st.error("Booking failed. Please try again.")
#                         break
#                     remaining_beds = remaining_beds - beds_to_take

#                 if remaining_beds == 0:
#                       # st.success("Booking Confirmed Successfully")
#                     hospital_id_query = """
#                         SELECT h_id FROM HOSPITAL WHERE h_name = %s
#                     """
#                     cursor.execute(hospital_id_query , (selected_hospitals,))
#                     hospital_id = cursor.fetchone()
                    

#                     insert_booking_query = """
#                         INSERT INTO BOOKINGS
#                         ( patient_name , h_id , resource_type , bed_type , quantity )
#                         VALUES(%s,%s,%s,%s,%s)
#                     """
#                     cursor.execute(
#                         insert_booking_query,
#                         (patient_name , hospital_id[0] , "Bed" , selected_bed_type , number_of_beds)
#                     )
#                     booking_id = cursor.lastrowid
#                     connection.commit()
#                     st.success("Booking Confirmed Successfully")

#                     st.write(f"**Booking ID:** {booking_id}")
#                     st.write(f"**Patient:** {patient_name}")
#                     st.write(f"**Hospital:** {selected_hospitals}")
#                     st.write(f"**Bed Type:** {selected_bed_type}")
#                     st.write(f"**Beds Booked:** {number_of_beds}")
#                 else:

#                     st.error(
#                         "Booking failed. Not enough beds available."
#                     )
#     else:

#         st.error("No beds are available for this bed type.")

# elif booking_type == "Ambulance" :
#     # st.write("You selected Ambulance Booking")
    
#     st.subheader("Ambulance Booking")

#     ambulance_query = """
#         SELECT DISTINCT ambulance_type
#         FROM AMBULANCES
#         WHERE h_id = (
#             SELECT h_id
#             FROM HOSPITAL
#             WHERE h_name = %s
#         )
#         AND status = 'Available'
#     """

#     cursor.execute(
#         ambulance_query,
#         (selected_hospitals,)
#     )

#     ambulances = cursor.fetchall()

#     ambulance_types = [row[0] for row in ambulances]

#     selected_ambulance_type = st.selectbox(
#         "Select ambulance type",
#         ambulance_types
#     )

#     availability_query = """
#         SELECT COUNT(*) FROM AMBULANCES
#         WHERE h_id = (
#             SELECT h_id
#             FROM HOSPITAL
#              WHERE h_name = %s
#         )
#         AND ambulance_type = %s
#         AND status = 'Available'
#     """

#     cursor.execute(availability_query , (selected_hospitals , selected_ambulance_type))
#     available_ambulances = cursor.fetchone()
#     available_count = available_ambulances[0]

#     if available_count > 0:
#         st.info(f"Available ambulances: {available_count}")

#         n_patient = st.text_input("Patient Name")
#         if st.button("Confirm Ambulance Booking") :

#             if n_patient.strip() == "" :
#                 st.warning("Please Enter The Patient Name")
#             else :
#                 ambulance_id_query = """
#                     SELECT A_id FROM AMBULANCES 
#                     WHERE h_id = (
#                         SELECT h_id FROM HOSPITAL
#                         WHERE h_name = %s 
#                     )
#                     AND ambulance_type = %s
#                     AND status = 'Available'
#                     LIMIT 1
#                 """

#                 cursor.execute(ambulance_id_query , (selected_hospitals, selected_ambulance_type))

#                 ambulance = cursor.fetchone()

#                 if ambulance:
#                     ambulance_id = ambulance[0] 

#                     # st.write(f"Ambulace id is : {ambulance_id}")
#                     updated_ambulance_query = """
#                         UPDATE AMBULANCES 
#                         SET status = 'Busy'
#                         WHERE A_id = %s
#                         AND status = 'Available'
#                     """
#                     cursor.execute(updated_ambulance_query , (ambulance_id,))
#                     if cursor.rowcount == 1:

#                         hospital_id_query = """
#                              SELECT h_id
#                              FROM HOSPITAL
#                              WHERE h_name = %s
#                         """

#                         cursor.execute(
#                         hospital_id_query,
#                         (selected_hospitals,)
#                         )

#                         hospital_id = cursor.fetchone()

#                         insert_booking_query = """
#                             INSERT INTO BOOKINGS
#                             (patient_name, h_id, resource_type, bed_type, quantity,  A_id)
#                             VALUES (%s, %s, %s, %s, %s , %s)
#                         """

#                         cursor.execute(
#                             insert_booking_query,
#                             (
#                                 n_patient,
#                                 hospital_id[0],
#                                 "Ambulance",
#                                 None,
#                                 1,
#                                 ambulance_id
#                             )
#                         )
#                         booking_id = cursor.lastrowid

#                         connection.commit()

#                         st.success("Ambulance booked successfully!")

#                         st.write(f"**Booking ID:** {booking_id}")
#                         st.write(f"**Patient:** {n_patient}")
#                         st.write(f"**Hospital:** {selected_hospitals}")
#                         st.write(f"**Ambulance Type:** {selected_ambulance_type}")
#                         st.write(f"**Ambulance ID:** {ambulance_id}")
#                     else:
#                         connection.rollback()
#                         st.error("Booking failed. Please try again.")


#                 else:
#                     st.error("No ambulance is available for booking.")
#     else:
#         st.error("No ambulances are currently available.")

# # st.write("You selected:" , selected_city)
# # st.write("You selected:" , selected_hospitals)
# # st.write(hospitals)

# # cursor.close()
# # connection.close()

import streamlit as st

st.set_page_config(
    page_title="Hospital Resource Intelligence",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Resource Intelligence")
st.caption("Smart hospital resource monitoring & real-time booking")

st.divider()

st.markdown("### Welcome 👋")
st.write(
    "A centralized platform to monitor hospital resources, "
    "availability, and manage real-time bookings."
)

st.markdown("#### Explore")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Dashboard")
    st.write("Monitor beds, ICUs, doctors, ambulances, OTs and hospital availability.")
    if st.button("Open Dashboard →", use_container_width=True):
        st.switch_page("pages/dashboard.py")

with col2:
    st.subheader("📝 Booking")
    st.write("Book available beds and ambulances directly from the system.")
    if st.button("Open Booking →", use_container_width=True):
        st.switch_page("pages/Booking.py")

st.divider()

