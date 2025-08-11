import random
from flask import Flask, request, jsonify
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# OpenTelemetry setup
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "rolldice-app"})
    )
)
otlp_exporter = OTLPSpanExporter(endpoint="http://10.255.255.254:4318/v1/traces")
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@app.route("/rolldice")
def rolldice():
    player = request.args.get("player", "anonymous")
    result = random.randint(1, 6)
    return jsonify({"player": player, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
