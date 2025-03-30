use std::collections::HashMap;

use qmetaobject::prelude::*;
use sailors::sailfishapp::QmlApp;


#[derive(Default, QObject)]
struct MyListModel {
    base: qt_base_class!(trait QAbstractListModel),
}

impl QAbstractListModel for MyListModel {
    fn row_count(&self) -> i32 {
        return 20;
    }

    fn data(&self, index: QModelIndex, role: i32) -> QVariant {
        match role {
            0 => index.row().into(),
            1 => QString::from("Hello").into(),
            _ => QVariant::default(),
        }
    }

    fn role_names(&self) -> HashMap<i32, QByteArray> {
        let mut res: HashMap<i32, QByteArray> = HashMap::new();
        res.insert(0, "index".into());
        res.insert(1, "message".into());
        res
    }
}

fn main() -> anyhow::Result<()> {
    let mut app = QmlApp::application("%{ProjectName}".into());
    let version: QString = env!("CARGO_PKG_VERSION").into();

    let my_list_model = QObjectBox::new(MyListModel::default());

    app.set_title("%{ProjectName}".into());
    app.set_application_version(version.clone());
    // app.install_default_translator().unwrap();
    app.set_source(QmlApp::path_to("qml/%{ProjectName}.qml".into()));

    app.set_object_property("MyListModel".into(), my_list_model.pinned());

    app.show_full_screen();

    qmeta_async::run(|| {
        app.exec()
    })
}
