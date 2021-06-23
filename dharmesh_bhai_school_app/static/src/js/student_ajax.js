console.log("Hello World!!!");


function get_data()
{
    console.log("get data called...");

    //'GET' - /school_app/get_data -> table
    $.ajax({
        url: '/school_app/get_data',
        type: 'GET',
        success: function (response)
        {
            console.log(response);
            console.log(typeof (response));
            
            console.table(JSON.parse(response).students);

            var student_recs = JSON.parse(response).students;

            console.table(student_recs)


            //students rec - > show table
            $('#tbody').html("")
            table_trs = ''
            student_recs.forEach(student => {
                // console.log(student)
                console.log(student.first_name);
                table_trs += '<tr><td>' +
                    student.first_name + '</td><td>' +
                    student.last_name + '</td><td>' +
                    student.gender + '</td><td>' +
                    student.mobile_no + '</td><td>' +
                    student.email_id + '</td></tr>';
            });

            //jquey
            $('#tbody').html(table_trs);

            //js
            // tbody_ele = document.getElementById('tbody');
            // tbody_ele.insertAdjacentHTML('beforeend',table_trs);


        }
        
    })
    
}

$('#studentForm').submit(function (e) {
    e.preventDefault();
    form = $(this);
    
    console.log(form);
    console.log(form.serialize());
    console.log(typeof (form.serialize())); //string
    

    $.ajax({
        url: '/add-student-ajax',
        type: 'POST',
        data: form.serialize(),
    
        success: function (response)
        {
            console.log(response);
            console.log(JSON.parse(response).message);

        }

    })


    console.log("form submitted...");
});