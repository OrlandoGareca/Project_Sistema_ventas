var tblClient;
function getData() {
     tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "dni"},
            {"data": "date_birthday"},
            {"data": "gender.name"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {
    modal_title = $('.modal-title');
    getData();

    $('.btnAdd').on('click', function (){

        $('input[name="action"]').val('add')
        modal_title.find('span').html('Creacion de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    });

    $('#data tbody')
        .on('click', 'a[rel="edit"]', function () {
        modal_title.find('span').html('Edicion de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblClient.cell($(this).closest('td,li')).index();
        var data = tblClient.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="dni"]').val(data.dni);
        $('input[name="date_birthday"]').val(data.date_birthday);
        $('input[name="address"]').val(data.address);
        $('input[name="gender"]').val(data.gender.id);
        $('#myModalClient').modal('show');
    })
        .on('click', 'a[rel="delete"]', function () {
        modal_title.find('span').html('Edicion de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tblClient.cell($(this).closest('td,li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action','delete');
            parameters.append('id',data.id);
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de eliminar el  siguiente registro?', parameters, function () {

                getData();
                tblClient.ajax.reload();
            });
    });

    $('#myModalClient').on('shown.bs.modal',function () {
        //$('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);

        // parameters.forEach(function (value, key) {
        //     console.log(key + ':' + value);
        // })
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalClient').modal('hide');
            getData();
            tblClient.ajax.reload();
            //location.href = '{{ list_url }}';
        });
    });
});