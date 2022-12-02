// Code generated by go-swagger; DO NOT EDIT.

package recurring_run_service

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"
)

// NewEnableRecurringRunParams creates a new EnableRecurringRunParams object
// with the default values initialized.
func NewEnableRecurringRunParams() *EnableRecurringRunParams {
	var ()
	return &EnableRecurringRunParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewEnableRecurringRunParamsWithTimeout creates a new EnableRecurringRunParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewEnableRecurringRunParamsWithTimeout(timeout time.Duration) *EnableRecurringRunParams {
	var ()
	return &EnableRecurringRunParams{

		timeout: timeout,
	}
}

// NewEnableRecurringRunParamsWithContext creates a new EnableRecurringRunParams object
// with the default values initialized, and the ability to set a context for a request
func NewEnableRecurringRunParamsWithContext(ctx context.Context) *EnableRecurringRunParams {
	var ()
	return &EnableRecurringRunParams{

		Context: ctx,
	}
}

// NewEnableRecurringRunParamsWithHTTPClient creates a new EnableRecurringRunParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewEnableRecurringRunParamsWithHTTPClient(client *http.Client) *EnableRecurringRunParams {
	var ()
	return &EnableRecurringRunParams{
		HTTPClient: client,
	}
}

/*EnableRecurringRunParams contains all the parameters to send to the API endpoint
for the enable recurring run operation typically these are written to a http.Request
*/
type EnableRecurringRunParams struct {

	/*RecRunID
	  The ID of the recurring runs to be enabled.

	*/
	RecRunID string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the enable recurring run params
func (o *EnableRecurringRunParams) WithTimeout(timeout time.Duration) *EnableRecurringRunParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the enable recurring run params
func (o *EnableRecurringRunParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the enable recurring run params
func (o *EnableRecurringRunParams) WithContext(ctx context.Context) *EnableRecurringRunParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the enable recurring run params
func (o *EnableRecurringRunParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the enable recurring run params
func (o *EnableRecurringRunParams) WithHTTPClient(client *http.Client) *EnableRecurringRunParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the enable recurring run params
func (o *EnableRecurringRunParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithRecRunID adds the recRunID to the enable recurring run params
func (o *EnableRecurringRunParams) WithRecRunID(recRunID string) *EnableRecurringRunParams {
	o.SetRecRunID(recRunID)
	return o
}

// SetRecRunID adds the recRunId to the enable recurring run params
func (o *EnableRecurringRunParams) SetRecRunID(recRunID string) {
	o.RecRunID = recRunID
}

// WriteToRequest writes these params to a swagger request
func (o *EnableRecurringRunParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param rec_run_id
	if err := r.SetPathParam("rec_run_id", o.RecRunID); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
