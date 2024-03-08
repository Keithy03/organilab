const get_multiple_text = (data) => {
    result = data.map(obj => obj.text);
    return result.join(", ");
}

const render_file = (data) => {
    if(data){
        return `<a href="${data.url}" title="${data.display_name}" download class="btn btn-outline-success"><i class="fa fa-download"></i> ${gettext("Download")}</a>`
      }
    return data;
}
table_default_dom = "<'row mb-1'<'col-sm-4 col-md-4 d-flex align-items-center justify-content-start'f>" +
                    "<'col-sm-4 col-md-4 d-flex align-items-center justify-content-center'B>" +
                    "<'col-sm-3 col-md-3 d-flex align-items-center justify-content-end 'l>>" +
                    "<'row'<'col-sm-12'tr>><'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>";

maintenance_datatable_inits = {
				columns: [
						{data: "id", name: "id", title: gettext("Id"), type: "string", visible: false},
						{data: "maintenance_date", name:"maintenance_date", title: gettext("Date"), type: "string", visible: true},
						{data: "provider_of_maintenance", name: "provider_of_maintenance", title: gettext("Provider"), type: "string", visible: true,
						render: data => data['text']},
						{data: "validator", name: "validator", title: gettext("Validator"), type: "string", visible: true, render: data=> data["text"]},
						{data: "maintenance_observation", name: "maintenance_observation", title: gettext("Observation"), type: "string", visible: true},
						{data: "actions", name: "actions", title: gettext("Actions"), type: "string", visible: true}
						],
		    	addfilter: true,
			    dom: table_default_dom
			    }

var logs_datatable_inits = {
				columns: [
						{data: "id", name: "id", title: gettext("Id"), type: "string", visible: false},
						{data: "last_update", name:"last_update", title: gettext("Date"), type: "date", visible: true, render: DataTable.render.datetime()},
						{data: "description", name: "description", title: gettext("Description"), type: "string", visible: true},
						{data: "actions", name: "actions", title: gettext("Actions"), type: "string", visible: true}
						],
		    	addfilter: true,
			    dom: table_default_dom
			    }


var calibrate_datatable_inits = {
				columns: [
						{data: "id", name: "id", title: gettext("Id"), type: "string", visible: false},
						{data: "calibration_date", name:"calibration_date", title: gettext("Date"), type: "date", visible: true},
						{data: "calibrate_name", name: "calibrate_name", title: gettext("Calibrator"), type: "string", visible: true},
						{data: "validator.text", name: "validator", title: gettext("Validator"), type: "string", visible: true},
						{data: "observation", name: "observation", title: gettext("Observation"), type: "string", visible: true},
						{data: "actions", name: "actions", title: gettext("Actions"), type: "string", visible: true}
						],
		    	addfilter: true,
			    dom: table_default_dom
			    }

var training_datatable_inits = {
				columns: [
						{data: "id", name: "id", title: gettext("Id"), type: "string", visible: false},
						{data: "training_initial_date", name:"training_initial_date", title: gettext("Initial date"), type: "date", visible: true},
						{data: "training_final_date", name:"training_final_date", title: gettext("Final date"), type: "date", visible: true},
						{data: "number_of_hours", name:"number_of_hours", title: gettext("Hours"), type: "number", visible: true},
						{data: "intern_people_receive_training", name:"intern_people_receive_training", title: gettext("Internal people"),
						type: "string", visible: true, render: data => get_multiple_text(data)},
						{data: "observation", name:"observation", title: gettext("Observation"), type: "string", visible: true},
						{data: "actions", name: "actions", title: gettext("Actions"), type: "string", visible: true}
						],
		    	addfilter: true,
			    dom: table_default_dom
			    }

var guarantee_datatable_inits = {
				columns: [
						{data: "id", name: "id", title: gettext("Id"), type: "string", visible: false},
						{data: "guarantee_initial_date", name:"guarantee_initial_date", title: gettext("Initial date"), type: "date", visible: true},
						{data: "guarantee_final_date", name:"guarantee_final_date", title: gettext("Final date"), type: "date", visible: true},
						{data: "contract", name:"contract", title: gettext("Contract"), type: "date", visible: true, render: data=> render_file(data)},
						{data: "actions", name: "actions", title: gettext("Actions"), type: "string", visible: true}
						],

			    dom: table_default_dom
			    }

var maintenance_modalids = {
    		create: "#create_maintenance_modal",
			destroy: "#delete_maintenance_modal",
			update: "#update_maintenance_modal"
}
var guarantee_modalids = {
    		create: "#create_guarantee_modal",
			destroy: "#delete_guarantee_modal",
			update: "#update_guarantee_modal"
}

var log_modalids = {
    		create: "#create_log_modal",
    		update: "#update_log_modal",
    		destroy: "#delete_log_modal",
    		}

var calibrate_modalids = {
    		create: "#create_calibrate_modal",
    		update: "#update_calibrate_modal",
    		destroy: "#delete_calibrate_modal",
    		}

var training_modalids = {
    		create: "#create_training_modal",
    		update: "#update_training_modal",
    		destroy: "#delete_training_modal",
    		}

var actions_log = {
		    table_actions: [],  //table_actions
			object_actions: [],
			title: gettext('Actions'),
			className:  "no-export-col"
}

var actions = {
		    table_actions: [],  //table_actions
			object_actions: [],
			title: gettext('Actions'),
			className:  "no-export-col"
}
var calibrate_actions = {
		    table_actions: [],  //table_actions
			object_actions: [],
			title: gettext('Actions'),
			className:  "no-export-col"
}

var guarantee_actions = {
		    table_actions: [],  //table_actions
			object_actions: [],
			title: gettext('Actions'),
			className:  "no-export-col"
}
var training_actions = {
		    table_actions: [],  //table_actions
			object_actions: [],
			title: gettext('Actions'),
			className:  "no-export-col"
}


icons= {
        create: '<i class="fa fa-plus" aria-hidden="true"></i>',
		clear: '<i class="fa fa-eraser" aria-hidden="true"></i>',
		update: 'fa fa-edit me-1 fa-lg',
		destroy: 'fa fa-trash fa-lg'
}

let maintenance_objconfig={
		urls: object_urls["maintenance"],
		datatable_element: "#maintenance_table",
		modal_ids: maintenance_modalids,
		actions: actions,
		datatable_inits: maintenance_datatable_inits,
		add_filter: true,
		relation_render: {'field_autocomplete': 'text' },
		delete_display: data => data['maintenance_observation'],
		create: "btn-success",
		icons: icons
}


let maintenance_ocrud = ObjectCRUD("maintenancecrudobj", maintenance_objconfig)
maintenance_ocrud.init();


let log_objconfig={
		urls: object_urls["log"],
		datatable_element: "#log_table",
		modal_ids: log_modalids,
		actions: actions_log,
		datatable_inits: logs_datatable_inits,
		add_filter: true,
		relation_render: {'field_autocomplete': 'text' },
		delete_display: data => data['description'],
		create: "btn-success",
		icons: icons
}

let log_ocrud = ObjectCRUD("logcrudobj", log_objconfig)
log_ocrud.init();


let calibrate_objconfig={
		urls: object_urls["calibrate"],
		datatable_element: "#calibrate_table",
		modal_ids: calibrate_modalids,
		actions: calibrate_actions,
		datatable_inits: calibrate_datatable_inits,
		add_filter: true,
		relation_render: {'field_autocomplete': 'text' },
		delete_display: data => data["calibration_date"]+" "+data['calibrate_name'],
		create: "btn-success",
		icons: icons
}

let calibrate_ocrud = ObjectCRUD("calibratecrudobj", calibrate_objconfig)
calibrate_ocrud.init();


let guarantee_objconfig={
		urls: object_urls["guarantee"],
		datatable_element: "#guarantee_table",
		modal_ids: guarantee_modalids,
		actions: guarantee_actions,
		datatable_inits: guarantee_datatable_inits,
		add_filter: true,
		relation_render: {'field_autocomplete': 'text' },
		delete_display: data => data["guarantee_initial_date"]+" - "+data['guarantee_final_date'],
		create: "btn-success",
		icons: icons
}

let guarantee_ocrud = ObjectCRUD("guaranteecrudobj", guarantee_objconfig)
guarantee_ocrud.init();


let training_objconfig={
		urls: object_urls["training"],
		datatable_element: "#training_table",
		modal_ids: training_modalids,
		actions: training_actions,
		datatable_inits: training_datatable_inits,
		add_filter: true,
		relation_render: {'field_autocomplete': 'text' },
		delete_display: data => data["training_initial_date"]+" - "+data['training_final_date'],
		create: "btn-success",
		icons: icons
}

let training_ocrud = ObjectCRUD("trainingcrudobj", training_objconfig)
training_ocrud.init();


