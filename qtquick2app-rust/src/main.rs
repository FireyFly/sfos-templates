use qmetaobject::prelude::*;
use sailors::sailfishapp::QmlApp;

fn main() {
    let mut app = QmlApp::application("%{ProjectName}".into());
    let version: QString = env!("CARGO_PKG_VERSION").into();

    app.set_title("%{ProjectName}".into());
    app.set_application_version(version.clone());
    // app.install_default_translator().unwrap();
    app.set_source(QmlApp::path_to("qml/%{ProjectName}.qml".into()));

    app.show_full_screen();

    qmeta_async::run(|| {
        app.exec()
    })
    .unwrap()
}
